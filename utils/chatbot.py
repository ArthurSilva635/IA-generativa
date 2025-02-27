from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain.embeddings.base import Embeddings
import google.generativeai as genai
import os


from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

load_dotenv()

# Carregar chave da API-key do Gemini e Google_credentials
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

# configuração da chave API (api_key) para consumir modelos como o Gemini 1.5 (da Google DeepMind). 
genai.configure(api_key=api_key)


def create_vectorstore(chunks):
    # Inicializa o modelo de embeddings Gemini
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001", # Esse modelo é otimizado para gerar embeddings semânticos.
        task_type="retrieval_document",
    )  

    # GoogleGenerativeAIEmbeddings → Usa o modelo Gemini para gerar embeddings.
    # FAISS → Cria o banco vetorial para fazer busca semântica.
    # from_texts → Converte os textos em vetores e armazena no FAISS.
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings) # Cria o banco vetorial para fazer busca semântica.
    print("Vectorstore criado com sucesso!")
    
    return vectorstore



def create_conversation_chain(vectorstore):
    model_Gemini = ChatGoogleGenerativeAI(
        model= "gemini-2.0-flash",
        temperature=0.2,
    )
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages= True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        model_Gemini,
        retriever = vectorstore.as_retriever(),
        memory = memory
    )
    return conversation_chain