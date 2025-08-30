# Answers 2.6

## Theory
1. Three stages of RAG‑QA: accept the query, retrieve relevant documents, and generate the answer.
2. Context window constraints: because the LLM context is limited, you cannot pass every fragment. MapReduce and Refine help aggregate or iteratively refine information across multiple documents.
3. Vector database: stores document embeddings and provides fast retrieval of the most relevant documents based on semantic similarity.
4. RetrievalQA chain: combines retrieval and answer generation, improving relevance and accuracy of results.
5. MapReduce and Refine: MapReduce quickly produces a summary from many documents; Refine sequentially improves the answer, which is useful when precision is critical. Choose based on the task.
6. Distributed systems: account for network latency and serialization when operating in distributed setups.
7. Experimentation: try MapReduce and Refine; effectiveness depends heavily on data types and question styles.
8. RetrievalQA limitation: no built‑in dialogue memory, which makes maintaining context across follow‑ups difficult.
9. Dialogue memory: needed to incorporate previous turns and provide contextual answers during longer conversations.
10. Further study: new LLM approaches, their impact on RAG systems, and memory strategies in RAG chains.

## Practical Tasks
1.
```python
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def initialize_vector_database(directory_path):
    # Initialize an embeddings generator (OpenAI) to create vector representations for text
    embeddings_generator = OpenAIEmbeddings()

    # Initialize a Chroma vector database pointing to a persistence directory
    # and the embedding function to use
    vector_database = Chroma(persist_directory=directory_path, embedding_function=embeddings_generator)

    # Display current document count to verify initialization
    # Assumes Chroma exposes `_collection.count()`
    document_count = vector_database._collection.count()
    print(f"Documents in VectorDB: {document_count}")

# Example usage of initialize_vector_database:
documents_storage_directory = 'path/to/your/directory'
initialize_vector_database(documents_storage_directory)
```

2.
```python
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def setup_retrieval_qa_chain(model_name, documents_storage_directory):
    # Initialize embeddings and Chroma vector store
    embeddings_generator = OpenAIEmbeddings()
    vector_database = Chroma(persist_directory=documents_storage_directory, embedding_function=embeddings_generator)

    # Initialize the language model (LLM) used in the RetrievalQA chain
    language_model = ChatOpenAI(model=model_name, temperature=0)

    # Define a custom prompt template to format LLM inputs
    custom_prompt_template = """To better assist with the inquiry, consider the details provided below as your reference...
{context}
Inquiry: {question}
Insightful Response:"""

    # Create the RetrievalQA chain, passing the LLM, a retriever from the vector DB,
    # requesting source documents, and using the custom prompt
    question_answering_chain = RetrievalQA.from_chain_type(
        language_model,
        retriever=vector_database.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": PromptTemplate.from_template(custom_prompt_template)}
    )

    return question_answering_chain

# Example usage of setup_retrieval_qa_chain:
model_name = "gpt-4o-mini"
documents_storage_directory = 'path/to/your/documents'
qa_chain = setup_retrieval_qa_chain(model_name, documents_storage_directory)
```

3.
```python
# Assume setup_retrieval_qa_chain has been defined in the same script or imported.

# Configure to demonstrate both techniques (MapReduce and Refine)
model_name = "gpt-3.5-turbo"
documents_storage_directory = 'path/to/your/documents'
qa_chain = setup_retrieval_qa_chain(model_name, documents_storage_directory)

# Create QA chains: one for MapReduce, one for Refine
question_answering_chain_map_reduce = RetrievalQA.from_chain_type(
    qa_chain.llm,
    retriever=qa_chain.retriever,
    chain_type="map_reduce"  # Use MapReduce chain type
)

question_answering_chain_refine = RetrievalQA.from_chain_type(
    qa_chain.llm,
    retriever=qa_chain.retriever,
    chain_type="refine"  # Use Refine chain type
)

# Example query to test both techniques
query = "What is the importance of probability in machine learning?"

# Run MapReduce and print the answer
response_map_reduce = question_answering_chain_map_reduce({"query": query})
print("MapReduce answer:", response_map_reduce["result"])

# Run Refine and print the answer
response_refine = question_answering_chain_refine({"query": query})
print("Refine answer:", response_refine["result"])
```

4.
```python
def handle_conversational_context(initial_query, follow_up_query, qa_chain):
    """
    Simulate handling a follow‑up question in a longer conversation.

    Args:
    - initial_query (str): First user query.
    - follow_up_query (str): Follow‑up query referring to prior context.
    - qa_chain (RetrievalQA): Initialized QA chain that can answer queries.

    Returns:
    - None: Prints both answers directly to the console.
    """
    # Generate the answer to the initial query
    initial_response = qa_chain({"query": initial_query})
    print("Answer to initial query:", initial_response["result"])

    # Generate the answer to the follow‑up query (note: no dialogue memory)
    follow_up_response = qa_chain({"query": follow_up_query})
    print("Answer to follow‑up query:", follow_up_response["result"])

# Example usage
a_initial = "Does the curriculum cover probability theory?"
a_follow_up = "Why are those prerequisites important?"
handle_conversational_context(a_initial, a_follow_up, qa_chain)
```
