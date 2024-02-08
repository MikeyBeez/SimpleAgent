from langchain.llms import Ollama
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GPT4AllEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import gradio as gr

def process_url_and_question(url: str, question: str):
    loader = WebBaseLoader(url)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    all_splits = text_splitter.split_documents(data)
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())

    ollama = Ollama(base_url="http://localhost:11434", model="nous-hermes2:latest")
    qachain = RetrievalQA.from_chain_type(ollama, retriever=vectorstore.as_retriever())

    result = qachain({"query": question})
    return result

iface = gr.Interface(fn=process_url_and_question, 
                     inputs=["text", "text"], 
                     outputs="text")
iface.launch()

