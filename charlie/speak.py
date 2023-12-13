# speak.py

import subprocess
from gtts import gTTS

# Function to speak text using the say command
def speak_say(text):
    subprocess.run(['say', text])

# Function to speak text using gTTS
def speak_gtts(text):
    tts = gTTS(text=text, lang='en')
    tts.save("speak.mp3")
    subprocess.run(['mpg123', 'speak.mp3'])

