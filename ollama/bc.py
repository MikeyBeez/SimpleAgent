import argparse
import time
from langchain.llms import Ollama
from colorama import init, Fore, Back, Style

class Agent:
    def __init__(self, name, color):
        self.ollama = Ollama()
        self.name = name
        self.color = color

    def generate_response(self, prompt):
        response = self.ollama(prompt)
        return response

    def agent(self, prompt):
        agent_output = self.generate_response(prompt)
        content = f"{self.color}{self.name} replies: {agent_output}{Style.RESET_ALL}"
        print(content)
        return agent_output

    def run_conversation(self, conversation_duration, initial_prompt, other_agent):
        conversation_history = [{"role": "system", "content": "Always answer with concise replies."}, {"role": "user", "content": initial_prompt}]

        print(f"Initial Prompt: {initial_prompt}\n")

        prompt = initial_prompt
        start_time = time.time()

        while time.time() - start_time < conversation_duration:
            # Agent's turn
            agent_output = self.agent(prompt)
            conversation_history.append({"role": "user", "content": prompt})
            conversation_history.append({"role": "assistant", "content": agent_output})

            print(f"{other_agent.color}User replies: {prompt}{Style.RESET_ALL}\n")

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
        agent1 = Agent("Agent1", Fore.GREEN)
        agent2 = Agent("Agent2", Fore.BLUE)

        agent1.run_conversation(args.duration, args.initial_prompt, agent2)

