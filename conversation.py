import time
from langchain.llms import Ollama  # Assuming this is the correct import for Ollama

def generate_response(ollama, prompt):
    response = ollama(prompt)
    return response

def agent_one(ollama, prompt):
    agent_output = generate_response(ollama, prompt)
    print(f"Agent 1: {agent_output}")
    return f"Agent 1 said: {agent_output}"

def agent_two(ollama, prompt):
    agent_output = generate_response(ollama, prompt)
    print(f"Agent 2: {agent_output}")
    return f"Agent 2 said: {agent_output}"

def run_conversation(ollama, conversation_duration, initial_prompt):
    conversation_history = []

    # Get the start time of the conversation
    start_time = time.time()

    # Start the conversation loop
    while time.time() - start_time < conversation_duration:
        # Agent One's turn
        agent_one_output = agent_one(ollama, initial_prompt if not conversation_history else conversation_history[-1])
        conversation_history.append(agent_one_output)
        time.sleep(1)

        # Check if the conversation duration has been reached
        if time.time() - start_time >= conversation_duration:
            break

        # Agent Two's turn
        agent_two_output = agent_two(ollama, conversation_history[-1])
        conversation_history.append(agent_two_output)
        time.sleep(1)

if __name__ == "__main__":
    # Assuming Ollama is properly instantiated with the correct parameters
    ollama = Ollama(base_url='http://localhost:11434', model="llama2")

    # Set the duration of the conversation in seconds and the initial prompt
    conversation_duration = 10
    initial_prompt = "Hello"

    run_conversation(ollama, conversation_duration, initial_prompt)

