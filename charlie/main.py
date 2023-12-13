# main.py

import argparse
from conversation import run_conversation  # Import run_conversation from conversation.py

# Main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run a conversation.')
    parser.add_argument('--duration', type=int, default=300, help='The duration of the conversation in seconds.')
    parser.add_argument('--initial_prompt', type=str, default='Hello, world!', help='The initial prompt for the conversation.')
    parser.add_argument('-g', '--use_gtts', action='store_true', help='Whether to use gTTS to speak the response.')
    args = parser.parse_args()

    run_conversation(args.duration, args.initial_prompt, args.use_gtts)

