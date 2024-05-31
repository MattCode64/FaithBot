from langchain_community.document_loaders import DirectoryLoader
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
import os
import shutil

DATA_PATH = "/home/matthieu/UbuntuData/PycharmProjects/FaithBot/Bible Data/All Books"
CHROMA_PATH = "chroma"

# Embedding :
embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
embedding = HuggingFaceEmbeddings(model_name=embedding_model)


def load_documents() -> list[Document]:
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    print(f"Loaded {len(documents)} documents")
    print(f"Load Documents, Done!")
    return documents


def split_documents(documents: list[Document]):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True
    )

    chunks = splitter.split_documents(documents)
    print(f"Number of chunks: {len(chunks)} for {len(documents)} documents")

    document = chunks[3]
    # print(f"Page content : {document.page_content}")
    # print(f"Page number : {document.page_number}")
    # print(document.metadata)

    # print(type(chunks))
    print(f"Split Documents, Done!")
    return chunks


def save_to_chroma(chunks: list[Document]):
    print(f"Saving {len(chunks)} documents to Chroma {CHROMA_PATH} ...")
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    db = Chroma.from_documents(documents=chunks, embedding=embedding, persist_directory=CHROMA_PATH)
    db.persist()

    print(f"Saved {len(chunks)} documents to Chroma {CHROMA_PATH}")
    print(f"Save to Chroma, Done!")


def generate_database():
    documents = load_documents()
    chunks = split_documents(documents)
    save_to_chroma(chunks)
    print(f"Generate Database for RAG, Done!")


def main():
    print(f"Starting {main.__name__}")
    generate_database()


if __name__ == '__main__':
    main()
