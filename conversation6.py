
import argparse
import time
import requests
import json

def generate_response(prompt, context):
    r = requests.post('http://localhost:11434/api/generate',
                      json={
                          'model': 'llama2',
                          'prompt': prompt,
                          'context': context,
                      },
                      stream=True)
    r.raise_for_status()

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        print(response_part, end='', flush=True)

        if 'error' in body:
            raise Exception(body['error'])

        if body.get('done', False):
            return body['context']

def run_conversation(conversation_duration, initial_prompt):
    context = []  # the context stores a conversation history, you can use this to make the model more context aware
    start_time = time.time()

    while time.time() - start_time < conversation_duration:
        # Agent's turn
        context = generate_response(initial_prompt, context)
        time.sleep(6)

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
