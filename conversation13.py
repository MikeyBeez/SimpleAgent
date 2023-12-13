import argparse
import time
import requests
import json
import subprocess
from gtts import gTTS
import threading

# Function to speak text using the say command
def speak_say(text):
    subprocess.run(['say', text])

# Function to speak text using gTTS
def speak_gtts(text):
    tts = gTTS(text=text, lang='en')
    tts.save("speak.mp3")
    subprocess.run(['mpg123', 'speak.mp3'])

# Function to print colored text
def print_text(role, text):
    print(role.colored_text(text), end='', flush=True)

# Define a class for different roles in the conversation
class Role:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # Function to return colored text
    def colored_text(self, text):
        return f'\033[{self.color}m{text}\033[0m'

# Define different roles with their respective colors
advocate = Role('Advocate', '34')  # Blue text
critic = Role('Critic', '31')  # Red text
arbitrator = Role('Arbitrator', '33')  # Yellow text

# Function to generate a response from the model
def generate_response(prompt, context, role, use_gtts):
    # Send a POST request to the model server
    r = requests.post('http://localhost:11434/api/generate',
                      json={
                          'model': 'llama2',
                          'prompt': prompt,
                          'context': context,
                          'max_tokens': 50,  # Limit the response to 50 tokens
                      },
                      stream=True)
    r.raise_for_status()  # Raise an exception if the request failed

    # Process the response from the server
    response = ""
    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        response += response_part

        # Speak and print each word individually
        for word in response_part.split():
            if word.strip():  # Ensure the word is not empty or does not only contain whitespace
                if use_gtts:
                    speak_gtts(word)
                else:
                    speak_say(word)
            print(role.colored_text(word), end=' ', flush=True)

        # Raise an exception if there was an error in the response
        if 'error' in body:
            raise Exception(body['error'])

        # Return the response when it's done
        if body.get('done', False):
            return response

# Function to run the conversation
def run_conversation(conversation_duration, initial_prompt, use_gtts):
    context = []  # the context stores a conversation history, you can use this to make the model more context aware
    start_time = time.time()
    role = advocate  # Start with the advocate role
    prompt = initial_prompt
    roles = [advocate, critic, arbitrator]  # List of roles
    role_index = 0

    # Run the conversation for the specified duration
    while time.time() - start_time < conversation_duration:
        # Agent's turn
        print(f"\n{role.name}:")
        if role == advocate:
            role_prompt = f"what are three common arguments that support the idea that {prompt}.  Don't repeat an argument more than once unless it is to argue the point.  Try not to repeat yourself. Always support the idea.  You are an advocate.  Make certain that you don't repeat yourself.  do not repeatwhat the critic says.  Do not repeat what the arbitrator says."
        elif role == critic:
            role_prompt = f"what are three common arguments that critique the idea that {prompt}.  Don't repeat an argument more than once unless it is to argue the point.  Try not to repeat yourself. make sure you critique the idea and not support it."
        else:  # role == arbitrator
            role_prompt = f"what is a balanced perspective on the idea that {prompt} given the preceeding arguments.  Try not to repeat yourself. Do not answer as an advocate or a critic.  Instead try to be an impartial judge of all the arguments."
        prompt = generate_response(role_prompt, context, role, use_gtts)
        time.sleep(6)

        # Switch roles
        role_index = (role_index + 1) % len(roles)
        role = roles[role_index]

        # Break the loop when the conversation duration is over
        if time.time() - start_time >= conversation_duration:
            break

# Main function
if __name__ == "__main__":
    # Get the command-line arguments
    parser = argparse.ArgumentParser(description="Process two arguments.")
    parser.add_argument("--duration", type=int, help="Duration of the conversation in seconds")
    parser.add_argument("--initial_prompt", type=str, help="Initial prompt for the conversation")
    parser.add_argument('-g', '--gtts', action='store_true', help='use gTTS instead of say')

    args = parser.parse_args()

    # Run the conversation
    run_conversation(args.duration, args.initial_prompt, args.gtts)

