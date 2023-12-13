import argparse
import time
import requests
import json

class Role:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def colored_text(self, text):
        return f'\033[{self.color}m{text}\033[0m'

advocate = Role('Advocate', '34')  # Blue text
critic = Role('Critic', '31')  # Red text
arbitrator = Role('Arbitrator', '33')  # Yellow text

def generate_response(prompt, context, role):
    r = requests.post('http://localhost:11434/api/generate',
                      json={
                          'model': 'llama2',
                          'prompt': prompt,
                          'context': context,
                          'max_tokens': 50,  # Limit the response to 50 tokens
                      },
                      stream=True)
    r.raise_for_status()

    response = ""
    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        response += response_part
        print(role.colored_text(response_part), end='', flush=True)

        if 'error' in body:
            raise Exception(body['error'])

        if body.get('done', False):
            return response

def run_conversation(conversation_duration, initial_prompt):
    context = []  # the context stores a conversation history, you can use this to make the model more context aware
    start_time = time.time()
    role = advocate  # Start with the advocate role
    prompt = initial_prompt
    roles = [advocate, critic, arbitrator]  # List of roles
    role_index = 0

    while time.time() - start_time < conversation_duration:
        # Agent's turn
        print(f"\n{role.name}:")
        if role == advocate:
            role_prompt = f"what are three common arguments that support the idea that {prompt}.  Don't repeat an argument more than once unless it is to argue the point.  Try not to repeat yourself. Always support the idea.  You are an advocate.  Make certain that you don't repeat yourself.  do not repeatwhat the critic says.  Do not repeat what the arbitrator says."
        elif role == critic:
            role_prompt = f"what are three common arguments that critique the idea that {prompt}.  Don't repeat an argument more than once unless it is to argue the point.  Try not to repeat yourself. make sure you critique the idea and not support it."
        else:  # role == arbitrator
            role_prompt = f"what is a balanced perspective on the idea that {prompt} given the preceeding arguments.  Try not to repeat yourself. Do not answer as an advocate or a critic.  Instead try to be an impartial judge of all the arguments."
        prompt = generate_response(role_prompt, context, role)
        time.sleep(6)

        # Switch roles
        role_index = (role_index + 1) % len(roles)
        role = roles[role_index]

        if time.time() - start_time >= conversation_duration:
            break

if __name__ == "__main__":
    # Get the command-line arguments
    parser = argparse.ArgumentParser(description="Process two arguments.")
    parser.add_argument("--duration", type=int, help="Duration of the conversation in seconds")
    parser.add_argument("--initial_prompt", type=str, help="Initial prompt for the conversation")

    # Parse command-line arguments
    args = parser.parse_args()

    if args.duration is None or args.initial_prompt is None:
        print("Both --duration and --initial_prompt are required.")
    else:
        # Use the arguments in your program logic
        duration = args.duration
        initial_prompt = args.initial_prompt

        run_conversation(duration, initial_prompt)

