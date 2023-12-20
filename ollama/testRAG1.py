from langchain.llms import Ollama
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GPT4AllEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

loader = WebBaseLoader("https://arxiv.org/pdf/2303.03381.pdf")
data = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)
vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())

ollama = Ollama(base_url="http://localhost:11434", model="llama2")
qachain = RetrievalQA.from_chain_type(ollama, retriever=vectorstore.as_retriever())
question = "What are the top five main ideas in this paper?  Why is this paper important?"

result = qachain({"query": question})
print(result)
