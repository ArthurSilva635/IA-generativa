#from langchain.embeddings import OpenAIEmbeddings
#from langchain.vectorstores import FAISS

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain.embeddings.base import Embeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

import google.generativeai as genai
import os




# Carregar chave da API do Gemini
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
google_credentials = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Verificar se a chave foi carregada corretamente
if not api_key:
    raise ValueError("A chave da API do Gemini não foi encontrada. Verifique o arquivo .env.")
if not google_credentials:
    raise ValueError("As credenciais do Google não foram encontradas. Verifique a variável GOOGLE_APPLICATION_CREDENTIALS no arquivo .env.")

# Verificar se o arquivo JSON de credenciais do Google existe
if not os.path.exists(google_credentials):
    raise ValueError(f"O arquivo de credenciais do Google não foi encontrado no caminho especificado: {google_credentials}")

# Configurar a API
genai.configure(api_key=api_key)




class GeminiEmbeddings(Embeddings):
    """ Classe para gerar embeddings usando o modelo Gemini. """
    
    def embed_documents(self, texts):
        """ Gera embeddings para uma lista de textos. """
        return [self.get_embedding(text) for text in texts]

    def embed_query(self, text):
        """ Gera embeddings para um texto de consulta. """
        return self.get_embedding(text)

    def get_embedding(self, text):
        """ Função interna para chamar a API do Gemini e obter embeddings. """
        response = genai.embed_content(
            model="models/embedding-001",
            content=text,
            task_type="retrieval_document"
        )
        return response["embedding"]

def create_vectorstore(chunks):
    embeddings = GeminiEmbeddings()  # Inicializa o provedor de embeddings
    vectorstore = FAISS.from_texts(texts=chunks, embedding = embeddings)  # Cria o FAISS

    return vectorstore

def create_conversation_chain(vectorstore):
    model_Gemini = ChatGoogleGenerativeAI(
        model= "gemini-1.5-flash",
        temperature=0.2,
    )
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages= True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        model_Gemini,
        retriever = vectorstore.as_retriever(), # Buscador de tudo que é mais proximo
        memory = memory
    )
    return conversation_chain