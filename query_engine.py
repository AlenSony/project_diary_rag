# pyrefly: ignore [missing-import]
from langchain_chroma import Chroma
# pyrefly: ignore [missing-import]
from langchain_ollama import OllamaEmbeddings
# pyrefly: ignore [missing-import]
from langchain_ollama import ChatOllama

def ask_my_diary(user_question: str):
    embeddings = OllamaEmbeddings(model="llama3.1")
    db=Chroma(persist_directory="db_storage",embedding_function=embeddings)
    
    print(f"Searching database for context regarding: {user_question}..")
    matching_chunks = db.similarity_search(user_question, k=1)
    if not matching_chunks:
        print("No matching context found inside the database")
        return None
    retrieved_context = matching_chunks[0].page_content

    print(f"\n[Found matching data in {matching_chunks[0].metadata['source']}]")
    print(f"{retrieved_context}")

    local_llm = ChatOllama(model = "llama3.1", temperature = 0.0)
    
    #Prompt Construction

    engineered_prompt = (
        f"You are a development project archivist. Use ONLY the verified historical logs below to "
        f"answer the user's question accurately. If the context does not contain the answer, state explicitly "
        f"that you don't know.\n\n"
        f"Historical Logs Context:\n{retrieved_context}\n\n"
        f"User Question: {user_question}\n\n"
        f"Answer:"
    )

    #Genrating Response
    response = local_llm.invoke(engineered_prompt)
    return response

    #Testing the query function
# Update the bottom block to this:
if __name__ == "__main__":
    question = input("Ask about your project: ")
    answer = ask_my_diary(question)
    if answer:
        # If it's a LangChain object, we grab .content; otherwise print string directly
        text_answer = answer.content if hasattr(answer, 'content') else answer
        print(f"\nLLM Answer: {text_answer}")
    
    