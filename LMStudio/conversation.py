import time
import argparse
import openai

def generate_response(prompt):
    result = openai.ChatCompletion.create(
        model="local-model",  # this field is currently unused
        messages=[
            {"role": "system", "content": "Always answer with concise replies."},
            {"role": "user", "content": prompt}
        ]
    )

    response = result.choices[0]
    return response

def agent_one(prompt):
    identifies1 = "You are a funny comic who gives concise answers"
    prompt = identifies1 + prompt
    agent_output = generate_response(prompt)
    # print(f"Agent 1 from agent_one: {agent_output}")
    content = agent_output['message']['content']
    print(f"Agent 1 content: {content}")
    return content

def agent_two(prompt):
    identifies2 = "You are a critic who questions results and makes concise helpful suggestions"
    prompt = identifies2 + prompt
    agent_output = generate_response(prompt)
    # print(f"Agent 2: {agent_output}")
    content = agent_output['message']['content']
    print(f"Agent 2 content: {content}")
    return content

def run_conversation(conversation_duration, initial_prompt):
    conversation_history = [initial_prompt]  # Initialize with the initial prompt
    prompt1 = initial_prompt
    agent_one_output = agent_one(prompt1)
    prompt2 = agent_one_output
    conversation_history.append(f"Agent 1 said: {agent_one_output}")
    # Get the start time of the conversation
    start_time = time.time()
    # Start the conversation loop
    while time.time() - start_time < conversation_duration:
        # Agent Two's turn
        print(f"prompt2 = {prompt2}")
        agent_two_output = agent_two(prompt2)
        # print(f"The value of agent_two_output is: {agent_two_output}")
        conversation_history.append(f"Agent 2 said: {agent_two_output}")
        prompt1 = agent_two_output
        # print(f"The value of prompt1 is: {prompt1}")
        time.sleep(1)

        # Check if the conversation duration has been reached
        if time.time() - start_time >= conversation_duration:
            break

        # Agent one's turn
        agent_one_output = agent_one(prompt1)
        conversation_history.append(f"Agent 1 said: {agent_one_output}")
        prompt2 = agent_one_output
        time.sleep(2)

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

        # Assuming LMStudio is properly instantiated with the correct parameters

        openai.api_base = "http://localhost:1234/v1"  # point to the local server
        openai.api_key = ""  # no need for an API key

        run_conversation(duration, initial_prompt)
