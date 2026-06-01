import os
# pyrefly: ignore [missing-import]
from langchain_chroma import Chroma
# pyrefly: ignore [missing-import]
from langchain_ollama import OllamaEmbeddings
# pyrefly: ignore [missing-import]
from langchain_text_splitters import RecursiveCharacterTextSplitter

def ingest_diary_notes():
    print("Starting ingestion process...")

    embeddings = OllamaEmbeddings(model="llama3.1") #defining our free llama model

    note_path = "data_vault/day1_notes.md" #our note file location

    if not os.path.exists(note_path):
        print(f"Error: Place a dummy file at {note_path} and try again.")
        return

    with open(note_path, "r", encoding="utf-8") as f:
        raw_text = f.read()
    
    if not raw_text.strip():
        print("Error: Note is empty.")
        return
    print("Successfully loaded note content")

    #Text Chunking

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    chunks = text_splitter.create_documents(
        texts=[raw_text],
        metadatas=[{"source": note_path,"date":"2026-06-01"}]
    )
    print(f"Successfullt broken down into {len(chunks)} chunks")

    print("Vectorizing text chunks and saving to db_storage partition..")
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./db_storage"
    )
    print("Ingestion complete. Database successfullt initialized offline")



# Testing chunking
if __name__ == "__main__":
    ingest_diary_notes()

    

        