import nltk 
from langchain_community.llms import Ollama

# ANSI escape codes for colors
NEON_GREEN = '\033[92m' 
RESET_COLOR = '\033[0m' 

# Download NLTK's PunktSentenceTokenizer 
nltk.download('punkt') 

llm = Ollama(model="llama2")
query = "Tell me a joke. Why did the bicycle fall over?" 

sentence_buffer = ""

for chunk in llm.stream(query):
    # Directly process the chunk since it's assumed to be a string 
    sentence_buffer += chunk  
    sentences = nltk.sent_tokenize(sentence_buffer) 

    if len(sentences) > 1: 
        print(NEON_GREEN + sentences[0] + RESET_COLOR) 
        sentence_buffer = " ".join(sentences[1:])  

# Print any remaining text at the end
if sentence_buffer:
    print(NEON_GREEN + sentence_buffer + RESET_COLOR) 

