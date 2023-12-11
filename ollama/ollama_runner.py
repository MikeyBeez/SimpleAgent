import subprocess

def run_ollama(model_name):
    # Build the Ollama command
    ollama_command = f"ollama run {model_name}"

    # Start Ollama as a subprocess
    process = subprocess.Popen(ollama_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

    # Enter the interactive loop
    while True:
        # Get user input for the prompt
        user_input = input("Enter prompt (type 'exit' to end): ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            break

        # Send the user input to Ollama
        process.stdin.write(user_input + '\n')
        process.stdin.flush()

        # Read and print the output from Ollama
        output, error = process.communicate()
        print("Ollama Output:", output.strip())
        print("Ollama Error:", error.strip())

    # Close the subprocess
    process.stdin.close()
    process.stdout.close()
    process.stderr.close()
    process.terminate()

if __name__ == "__main__":
    # Get the model name from the command line arguments
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <model_name>")
        sys.exit(1)

    model_name = sys.argv[1]

    # Run Ollama with the specified model
    run_ollama(model_name)

