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
    print(f"result: {result}")
    response = result.choices[0]
    return response

def agent(prompt):
    agent_output = generate_response(prompt)
    content = agent_output['message']['content']
    print(f"Agent replies: {content}")
    return content

def run_conversation(conversation_duration, initial_prompt):
    conversation_history = [initial_prompt]  # Initialize with the initial prompt
    initialQuestion = initial_prompt
    print(f"Initial Prompt: {initialQuestion}")
    print("\n")
    conversation_history.append(f"Initial Prompt: {initialQuestion}")
    print("\n")
    prompt = initial_prompt
    agent_output = agent(prompt)
    conversation_history.append(f"Agent said reply: {agent_output}")
    print("\n")
    prompt = agent_output
    # Get the start time of the conversation
    start_time = time.time()
    # Start the conversation loop
    while time.time() - start_time < conversation_duration:
        # Next Agent's turn
        agent_output = agent(prompt)
        conversation_history.append(f"Next Agent said: {agent_output}")
        print("\n")
        prompt = agent_output
        time.sleep(6)

        # Check if the conversation duration has been reached
        if time.time() - start_time >= conversation_duration:
            break

    # print("\nConversation History:")
    # for entry in conversation_history:
        # print(entry)

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
