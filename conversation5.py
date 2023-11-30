import argparse
import time  # We need time to control when the conversation ends.
from langchain.llms import Ollama  # oddly, this is the correct import for Ollama.

def generate_response(ollama, prompt):
    response = ollama(prompt)
    return response

def agent(prompt):
    agent_output = generate_response(ollama, prompt)
    content = agent_output
    print(f"Agent replies: {content}")
    return content

def run_conversation(conversation_duration, initial_prompt):
    conversation_history = [{"role": "system", "content": "Always answer with concise replies."}, {"role": "user", "content": initial_prompt}]

    print(f"Initial Prompt: {initial_prompt}\n")

    prompt = initial_prompt
    start_time = time.time()

    while time.time() - start_time < conversation_duration:
        # Agent's turn
        agent_output = agent(prompt)
        conversation_history.append({"role": "user", "content": prompt})
        conversation_history.append({"role": "assistant", "content": agent_output})

        print(f"Agent replies: {agent_output}\n")

        prompt = agent_output
        time.sleep(6)

        if time.time() - start_time >= conversation_duration:
            break

    print("\nConversation History:")
    for entry in conversation_history:
        print(entry)


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
        # For example, you can store them in variables:
        duration = args.duration
        initial_prompt = args.initial_prompt

        ollama = Ollama(base_url='http://localhost:11434', model="llama2")


        run_conversation(duration, initial_prompt)
