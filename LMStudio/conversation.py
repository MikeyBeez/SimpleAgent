import time
import argparse
import openai

def generate_response(prompt):
    result = openai.ChatCompletion.create(
        model="local-model", # this field is currently unused
        messages=[
            {"role": "system", "content": "Always answer in rhymes."},
            {"role": "user", "content": "Introduce yourself."}
        ]  
 )
 
    response = result.choices[0].message
    return response

def agent_one(prompt):
    role1 = "You are a funny comic who gives concise answers"
    prompt = role1 + prompt
    agent_output = generate_response(prompt)
    print(f"Agent 1: {agent_output}")
    return f"Agent 1 said: {agent_output}"

def agent_two(prompt):
    role2 = "You are a tic who questions results and makes concise helpful suggestions"
    prompt = role2 + prompt
    agent_output = generate_response(prompt)
    print(f"Agent 2: {agent_output}")
    return f"Agent 2 said: {agent_output}"

def run_conversation(conversation_duration, initial_prompt):
    conversation_history = [initial_prompt]  # Initialize with the initial prompt

    # Get the start time of the conversation
    start_time = time.time()

    # Start the conversation loop
    while time.time() - start_time < conversation_duration:
        # Agent One's turn
        agent_one_output = agent_one(conversation_history[-1])
        conversation_history.append(agent_one_output)
        time.sleep(1)

        # Check if the conversation duration has been reached
        if time.time() - start_time >= conversation_duration:
            break

        # Agent Two's turn
        agent_two_output = agent_two(conversation_history[-1])
        conversation_history.append(agent_two_output)
        time.sleep(1)

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

        # Assuming LMStudio is properly instantiated with the correct parameters
 
        openai.api_base = "http://localhost:1234/v1" # point to the local server
        openai.api_key = "" # no need for an API key


        run_conversation(duration, initial_prompt)
