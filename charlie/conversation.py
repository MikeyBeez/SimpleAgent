# conversation.py

import time
from roles import Role  # Import Role from roles.py
from response_generator import generate_response  # Import generate_response from response_generator.py

# Define different roles with their respective colors
advocate = Role('Advocate')  # Blue text
critic = Role('Critic')  # Red text
arbitrator = Role('Arbitrator')  # Yellow text

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
        with open(f'{role.name.lower()}.txt', 'r') as f:  # Open the role's text file
            prompt = f.read().strip()  # Read the prompt from the file
        response = generate_response(prompt, context, role, use_gtts)
        context.append((role.name, response))  # Add the role's name and response to the context

        # User's turn
        print("\nUser:")
        user_input = input()
        context.append(('User', user_input))  # Add the user's input to the context

        # Switch roles
        role_index = (role_index + 1) % len(roles)
        role = roles[role_index]

