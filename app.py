import streamlit as st
from utils import chatbot, text
from streamlit_chat import message


def main():

    st.set_page_config(page_title='Chat PDF TRE-RN', page_icon=':books:')

    st.header('Converse com seus arquivos')
    user_question = st.text_input("Faça uma pergunta para mim!")

    if('conversation' not in st.session_state):
        st.session_state.conversation = None

    if(user_question):
        response = st.session_state.conversation(user_question) ['chat_history'][-1]

        message(user_question, is_user=True)
        message(response.content, is_user=False)


    with st.sidebar:

        st.subheader('Seus arquivos')
        pdf_docs = st.file_uploader("Carregue seus arquivos em formato PDF aqui !", accept_multiple_files=True)

        if st.button('Processar'):
            all_files_text = text.process_files(pdf_docs)

            chunks = text.creat_text_chunks(all_files_text)

            vectorstore = chatbot.create_vectorstore(chunks)

            st.session_state.conversation = chatbot.create_conversation_chain(vectorstore)

if __name__ == '__main__':

    main()