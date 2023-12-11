import pexpect

def run_ollama(model_name):
    # Build the Ollama command
    ollama_command = f"ollama run {model_name}"

    # Start Ollama as a child process
    child = pexpect.spawn(ollama_command)

    # Enter the interactive loop
    while True:
        # Get user input for the prompt
        user_input = input("Enter prompt (type 'exit' to end): ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            break

        # Send the user input to Ollama
        child.sendline(user_input)

        # Read and print the output from Ollama
        while True:
            try:
                child.expect('\s, timeout=20')  # Expect any whitespace character
                print(child.before, end='')  # Print the output before the whitespace
            except pexpect.EOF:
                break  # Break the loop if the end of the output is reached

if __name__ == "__main__":
    # Get the model name from the command line arguments
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <model_name>")
        sys.exit(1)

    model_name = sys.argv[1]

    # Run Ollama with the specified model
    run_ollama(model_name)
