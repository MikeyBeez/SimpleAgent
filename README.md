# SimpleAgent

The idea behind this project is to help beginners write agents.  Current projects like autogen are not good starting examples for beginners.  There is too much code.  These examples should be easy to understand.  My hope is that, consequently, more people will write agents.

Conversation.py may be the simplest possible two agent program that uses a local model.  
I've also added some additional versions with increading complexityr; so conversation3.py is more complex than conversation2.py. I'm using Ollama to run local models as it is the simplest possible way to get started running local models.  

I won't give installation instructions here for Ollama.  You can find what you need at https://www.ollama.ai.  Understand however that Ollama needs to be running.  Then you do need to pip install ollama in your environment. If you have trouble, there are a lot of youtube videos for installing ollama.  

You also need to pip install langchain.

Starting a conversation:  python3 conversation4.py --duration 60 --initial_prompt "What's a good car to buy?"  

I've added a directory for LM Studio instead of Ollama. I need to set things like number of tokens, and as far as I can see, you can't do this in Ollama.  

Keep in mind that there are errors in these programs.  Some things will work, others will not.  Think about why there the program doesn't function exactly right.  Make a change or two.  Then go on to the next file.  I hope this will create an easy learning experience.   
