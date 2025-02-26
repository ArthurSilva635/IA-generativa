# 📚 AI Legal Chatbot - RAG-powered PDF Reader

Um chatbot baseado em *Deep Learning* e *Generative AI* com *Retrieval-Augmented Generation (RAG)*, capaz de processar PDFs de sentenças judiciais e simplificar consultas jurídicas.

## 🚀 Tecnologias Utilizadas

- **Linguagem**: Python 🐍  
- **Frameworks**: Streamlit  
- **Modelos**: LLMs (*gemini-1.5-flash*)  
- **Processamento de PDFs**: PyPDF2  
- **Busca Inteligente**: FAISS 
- **APIs de Chatbot**: LangChain / Gemini API  

## 📦 Instalação

Siga os passos abaixo para configurar o ambiente:

```bash
# Clone este repositório
git clone https://github.com/ArthurSilva635/IA-generativa

# Acesse a pasta do projeto
cd IA-generativa

# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Inicie o chatbot e abra no navegador
poetry run Streamlit run app.py #Linux/macOS

# Adicione os PDFs de sentenças e aperte e processar
![print da interface do projeto](/home/arthur_silva/Projetos_tre2024/projeto_Open_Langchain_Streamlit_RAG/utils/img/img1.PNG)

# Interaja com o chatbot via UI web.
-------------------

📊 Arquitetura do Projeto
Pré-processamento: Extração de texto dos PDFs.
Indexação: Vetorização dos documentos com embeddings + FAISS.
Geração de Respostas: Modelo LLMs (*gemini-1.5-flash*) aprimorado com RAG.
Interface: Streamlit para interação com usuários.
