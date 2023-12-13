# response_generator.py

import requests
import json
from speak import speak_say, speak_gtts  # Import functions from speak.py

# Function to generate a response from the model
def generate_response(prompt, context, role, use_gtts):
    # Send a POST request to the model server
    r = requests.post('http://localhost:11434/api/generate',
                      json={
                          'model': 'llama2',
                          'prompt': prompt,
                          'context': context,
                          'max_tokens': 50,  # Limit the response to 50 tokens
                      },
                      stream=True)
    r.raise_for_status()  # Raise an exception if the request failed

    # Process the response from the server
    response = ""
    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        response += response_part

        # Speak and print each word individually
        for word in response_part.split():
            if word.strip():  # Ensure the word is not empty or does not only contain whitespace
                if use_gtts:
                    speak_gtts(word)
                else:
                    speak_say(word)
            print(role.colored_text(word), end=' ', flush=True)

        # Raise an exception if there was an error in the response
        if 'error' in body:
            raise Exception(body['error'])

        # Return the response when it's done
        if body.get('done', False):
            return response

