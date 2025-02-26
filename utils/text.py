from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter


def process_files(files):

    text = ""

    for file in files:
        pdf = PdfReader(file)

        for page in pdf.pages:
            text += page.extract_text()

    return text

# Utilizando LAnchain para particionar um texto maior em textos menores (chuks)
def creat_text_chunks(text):

    text_splitter = CharacterTextSplitter(
        separator ='\n',        # Caractere usado para dividir os textos
        chunk_size = 1000 ,     # Descrevem o tamanho máximo que um único pedaço de chunk pode ter
        chunk_overlap = 100,    # Determina a quantidade de sobreposição que deve existir entre dois chunks consecutivos.
        length_function = len
    )

    chunks = text_splitter.split_text(text)
    return chunks


