# Answers 2.7

## Theory
1. Dialogue memory: provides a chatbot with context between messages, enabling more personalized and coherent answers.
2. `ConversationBufferMemory`: stores the entire conversation history so the model can refer to prior turns in the current dialogue.
3. Conversational Retrieval Chain: combines memory with retrieval from external sources to improve answer accuracy and relevance.
4. Context‑management strategies: range from fixed buffers to dynamically expanding context via document retrieval; the choice depends on the task.
5. NER (Named Entity Recognition): helps track key entities in the dialogue and maintain discussion integrity.
6. Data privacy: requires minimizing data collection, anonymizing sensitive information, and having transparent, lawful data‑retention policies.
7. Topic shifts: summarization, topic‑aware memory, and selective retrieval of the most relevant history can help when the subject changes.
8. Evaluation metrics: include user satisfaction, task success, and automated measures of coherence and relevance.
9. Persistent memory: useful for maintaining context across sessions, preserving user preferences and information about past issues and resolutions.
10. Practical recommendations: ensure privacy and transparency, give users control over memory, and continuously monitor interaction quality.

## Practical Tasks
1.
```python
def embed_document(document_text):
    """
    Stub function that generates a document embedding.
    In a real scenario, this should convert the input document text into a numeric vector representation.
    """
    # Simulated embedding for demonstration (simple hash based on text length/content)
    return [hash(document_text) % 100]

def create_vector_store(documents):
    """
    Convert a list of documents into embeddings and store them in a simple in‑memory structure.

    Args:
        documents (list of str): List of document texts to embed.

    Returns:
        list: List of generated embeddings representing the input documents.
    """
    vector_store = [embed_document(doc) for doc in documents]
    return vector_store

# Example usage of embed_document and create_vector_store:
documents = [
    "Document 1 text content here.",
    "Document 2 text content, possibly different.",
    "Another document, the third one."
]
vector_store = create_vector_store(documents)
print("Vector store:", vector_store)
```

2.
```python
def calculate_similarity(query_embedding, document_embedding):
    """
    Stub function to compute similarity between two embeddings.
    In practice, use metrics like cosine similarity or Euclidean distance.

    Args:
        query_embedding (list): Embedding of the search query.
        document_embedding (list): Embedding of a document.

    Returns:
        float: Simulated similarity score between query and document.
    """
    # Simplified similarity for demonstration
    return -abs(query_embedding[0] - document_embedding[0])

def perform_semantic_search(query, vector_store):
    """
    Perform semantic search to find the document most similar to the query within the vector store.

    Args:
        query (str): User’s search query.
        vector_store (list): In‑memory structure containing document embeddings.

    Returns:
        int: Index of the most similar document in `vector_store`.
    """
    query_embedding = embed_document(query)
    similarity_scores = [calculate_similarity(query_embedding, doc_embedding) for doc_embedding in vector_store]
    # Get the index of the document with the highest similarity score
    most_similar_index = similarity_scores.index(max(similarity_scores))
    return most_similar_index

# Example usage of calculate_similarity and perform_semantic_search:
query = "Document content that resembles document 1 more than others."
most_similar_doc_index = perform_semantic_search(query, vector_store)
print("Most similar document index:", most_similar_doc_index)
```

3.
```python
class Chatbot:
    def __init__(self):
        # Store chat history as a list of (query, response) tuples
        self.history = []

    def generate_response(self, query, context):
        """
        Stub function simulating answer generation based on the current user query
        and the provided context (chat history).

        Args:
            query (str): Current user query.
            context (list of tuples): List of (query, response) pairs representing chat history.

        Returns:
            str: Simulated chatbot response.
        """
        # For simplicity, produce a templated response that references history length
        return f"Response to '{query}' (with {len(context)} past interactions)."

    def respond_to_query(self, query):
        """
        Accept a user query, generate a response using current chat history,
        and update history with the new (query, response) pair.

        Args:
            query (str): User query.

        Returns:
            str: Generated chatbot response.
        """
        response = self.generate_response(query, self.history)
        # Update history with the latest interaction
        self.history.append((query, response))
        return response

# Example usage of Chatbot:
chatbot = Chatbot()
print(chatbot.respond_to_query("Hello, how are you?"))
print(chatbot.respond_to_query("What is the weather like today?"))
print(chatbot.respond_to_query("Thank you!"))
```

4.
```python
class LanguageModel:
    def predict(self, input_text):
        # Stub of the language model `predict` method; a real implementation would
        # call an actual LLM to generate the response.
        return f"Mock response for: {input_text}"

class DocumentRetriever:
    def retrieve(self, query):
        # Stub of `retrieve` for fetching documents; a real implementation
        # would search and return relevant documents by query.
        return f"Mock document related to: {query}"

class ConversationMemory:
    def __init__(self):
        # Initialize an empty list to store conversation history
        self.memory = []

    def add_to_memory(self, query, response):
        # Add a new (query, response) entry to memory
        self.memory.append((query, response))

    def reset_memory(self):
        # Clear the entire memory history
        self.memory = []

    def get_memory(self):
        # Return the current memory history
        return self.memory

def setup_conversational_retrieval_chain():
    # Initialize individual components for the retrieval chain:
    # language model, document retriever, and conversation memory.
    language_model = LanguageModel()
    document_retriever = DocumentRetriever()
    conversation_memory = ConversationMemory()

    # For demonstration, return a dict representing initialized components.
    # A real implementation would integrate them into a working system.
    retrieval_chain = {
        "language_model": language_model,
        "document_retriever": document_retriever,
        "conversation_memory": conversation_memory
    }
    return retrieval_chain

# Example usage of setup_conversational_retrieval_chain:
retrieval_chain = setup_conversational_retrieval_chain()
print(retrieval_chain)
```

5.
```python
class EnhancedChatbot(Chatbot):
    def __init__(self):
        super().__init__()
        # Initialize ConversationMemory (from the previous task) to manage chat history
        self.conversation_memory = ConversationMemory()

    def add_to_history(self, query, response):
        """
        Add a new (user query, chatbot response) entry to the conversation history
        using ConversationMemory.

        Args:
            query (str): User query.
            response (str): Chatbot response.
        """
        self.conversation_memory.add_to_memory(query, response)

    def reset_history(self):
        """
        Reset the entire conversation history, clearing all past interactions.
        """
        self.conversation_memory.reset_memory()

    def respond_to_query(self, query):
        """
        Override Chatbot.respond_to_query to include enhanced conversation‑memory handling.
        """
        # Generate a response using the base behavior and the current memory
        response = super().generate_response(query, self.conversation_memory.get_memory())
        # Update memory with the latest turn
        self.add_to_history(query, response)
        return response

# Example usage of EnhancedChatbot:
enhanced_chatbot = EnhancedChatbot()
print(enhanced_chatbot.respond_to_query("Hello, how are you?"))
enhanced_chatbot.reset_history()
print(enhanced_chatbot.respond_to_query("Starting a new conversation."))
```

6.
```python
def embed_document(document_text):
    # Stub for simulating a document text embedding. In a real system,
    # this would use an actual embedding model (e.g., OpenAI Embeddings).
    return sum(ord(char) for char in document_text) % 100  # Simple hash for demo

def split_document_into_chunks(document, chunk_size=100):
    # Split the input document text into manageable chunks of a given size
    return [document[i:i+chunk_size] for i in range(0, len(document), chunk_size)]

def perform_semantic_search(query_embedding, vector_store):
    # Find the most relevant document chunk in the vector store
    # based on embedding similarity. This is a placeholder search.
    similarities = [abs(query_embedding - chunk_embedding) for chunk_embedding in vector_store]
    return similarities.index(min(similarities))

def generate_answer_from_chunk(chunk):
    # Stub for simulating answer generation from a chosen document chunk.
    # A real system would use an LLM to formulate the answer.
    return f"Based on your question, a relevant piece of information is: \"{chunk[:50]}...\""

# Main logic of a simple document‑grounded Q&A system
document = "This is a long document. " * 100  # Simulated long document
chunks = split_document_into_chunks(document, 100)
vector_store = [embed_document(chunk) for chunk in chunks]

# Simulate a user question and its embedding
user_question = "What is this document about?"
question_embedding = embed_document(user_question)

# Find the most relevant document chunk to answer from
relevant_chunk_index = perform_semantic_search(question_embedding, vector_store)
relevant_chunk = chunks[relevant_chunk_index]

# Generate the answer based on the selected chunk
answer = generate_answer_from_chunk(relevant_chunk)
print(answer)
```

7.
```python
def integrate_memory_with_retrieval_chain(retrieval_chain, user_query):
    """
    Integrate a conversational retrieval chain with a memory system to maintain context
    during the dialogue.

    Args:
        retrieval_chain (dict): Mock retrieval chain containing the language model,
                                document retriever, and conversation memory.
        user_query (str): Current user query to process.
    """
    # Pull components from the provided retrieval chain
    conversation_memory = retrieval_chain["conversation_memory"]
    language_model = retrieval_chain["language_model"]
    document_retriever = retrieval_chain["document_retriever"]

    # Simulate using the retriever to fetch relevant information
    relevant_info = document_retriever.retrieve(user_query)

    # Get current history to use as context
    context = conversation_memory.get_memory()

    # Simulate response generation with the language model using the query,
    # context, and retrieved info
    response = language_model.predict(
        f"Query: {user_query}, Context: {context}, Relevant Info: {relevant_info}"
    )

    # Update memory with the new turn
    conversation_memory.add_to_memory(user_query, response)

    return response

# Use the retrieval chain from task 4 with a dummy query to demonstrate
dummy_query = "Tell me more about this document."
response = integrate_memory_with_retrieval_chain(retrieval_chain, dummy_query)
print("Generated response:", response)
```

8.
```python
def chatbot_cli():
    # Initialize EnhancedChatbot (extended chatbot from previous tasks with memory support)
    enhanced_chatbot = EnhancedChatbot()

    while True:
        print("\nOptions: ask [question], view history, reset history, exit")
        user_input = input("What would you like to do? ").strip().lower()

        if user_input.startswith("ask "):
            question = user_input[4:]
            response = enhanced_chatbot.respond_to_query(question)
            print("Chatbot:", response)
        elif user_input == "view history":
            for i, (q, a) in enumerate(enhanced_chatbot.conversation_memory.get_memory(), 1):
                print(f"{i}. Q: {q} A: {a}")
        elif user_input == "reset history":
            enhanced_chatbot.reset_history()
            print("Conversation history reset.")
        elif user_input == "exit":
            print("Exiting chatbot. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# To launch the chatbot CLI, uncomment the line below.
# (Commented to avoid auto‑execution in non‑interactive environments.)
# chatbot_cli()
```
