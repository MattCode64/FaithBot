from langchain_community.llms import Ollama
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

# Embedding :
embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
embedding = HuggingFaceEmbeddings(model_name=embedding_model)


def query_chroma(query_text: str):
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding)

    # Search in the database
    results = db.similarity_search_with_relevance_scores(query_text)
    # print(results)
    if len(results) == 0 or results[0][1] < 0.2:
        print("No relevant results found")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    user_prompt = prompt_template.format(context=context_text, question=query_text)
    print(f"Prompt: {user_prompt}")

    model = Ollama(model="mistral")
    response_text = model.invoke([HumanMessage(content=user_prompt)])

    sources = [doc.metadata["source"] for doc, _score in results]
    formatted_response = f"Response : {response_text}\nSources : {sources}"
    print(formatted_response)


def main():
    print(f"Starting {main.__name__}")
    query_chroma("How Noah's boat was made ?")


if __name__ == '__main__':
    main()
