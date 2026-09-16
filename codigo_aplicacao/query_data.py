import argparse
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

FAISS_PATH = "faiss"

def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    # Initialize LLM
    llm = OllamaLLM(model="llama3.1:8b")

    # Initialize embedding model
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")

    # Create vector object from local vector store
    vector = FAISS.load_local(FAISS_PATH, embeddings, allow_dangerous_deserialization=True)

    # Set up prompt
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""")

    # Set up retriever
    retriever = vector.as_retriever()

    # Retrieve documents
    documents = retriever.invoke(query_text)

    # Generate response using RAG
    context = "\n\n".join(document.page_content for document in documents)
    response = llm.invoke(prompt.format(context=context, input=query_text))

    print(response)


if __name__ == "__main__":
    main()
