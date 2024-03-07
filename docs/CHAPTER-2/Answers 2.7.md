# Answers 2.7

## Theory

## Practice
1.
```python
def embed_document(document_text):
    """
    Placeholder function for document embedding.
    In a real scenario, this function would convert document text into a numerical vector.
    """
    return [hash(document_text) % 100]  # Simulated embedding for demonstration purposes

def create_vector_store(documents):
    """
    Converts a list of documents into embeddings and stores them in a simple in-memory structure.

    Args:
        documents (list of str): List of document texts to be converted into embeddings.

    Returns:
        list: A list of embeddings representing the input documents.
    """
    vector_store = [embed_document(doc) for doc in documents]
    return vector_store

# Example usage
documents = [
    "Document 1 text content here.",
    "Document 2 text content, possibly different.",
    "Another document, the third one."
]
vector_store = create_vector_store(documents)
print("Vector Store:", vector_store)
```

2.
```python
def calculate_similarity(query_embedding, document_embedding):
    """
    Placeholder function for calculating similarity between two embeddings.
    In practice, this could use cosine similarity, Euclidean distance, etc.

    Args:
        query_embedding (list): The embedding of the query.
        document_embedding (list): The embedding of a document.

    Returns:
        float: A simulated similarity score between the query and the document.
    """
    # Simplified similarity calculation for demonstration
    return -abs(query_embedding[0] - document_embedding[0])

def perform_semantic_search(query, vector_store):
    """
    Performs a semantic search to find the document most similar to the query in the vector store.

    Args:
        query (str): The search query.
        vector_store (list): The in-memory structure storing document embeddings.

    Returns:
        int: The index of the most similar document in the vector store.
    """
    query_embedding = embed_document(query)
    similarity_scores = [calculate_similarity(query_embedding, doc_embedding) for doc_embedding in vector_store]

    # Finding the index of the highest similarity score
    most_similar_index = similarity_scores.index(max(similarity_scores))
    return most_similar_index

# Example usage
query = "Document content that resembles document 1 more than others."
most_similar_doc_index = perform_semantic_search(query, vector_store)
print("The most similar document index:", most_similar_doc_index)
```

3.
```python
class Chatbot:
    def __init__(self):
        # Initialize an empty list to store chat history, with each element being a tuple (query, response)
        self.history = []

    def generate_response(self, query, context):
        """
        Placeholder function to simulate response generation based on the current query and context.
        
        Args:
            query (str): The user's current query.
            context (list of tuples): The chat history, where each tuple contains a (query, response) pair.
            
        Returns:
            str: A simulated response.
        """
        # For simplicity, the response is just the query reversed with a note about the number of past interactions
        return f"Response to '{query}' (with {len(context)} past interactions)."

    def respond_to_query(self, query):
        """
        Takes a user's query as input, generates a response considering the chat history, and updates the history.

        Args:
            query (str): The user's query.
            
        Returns:
            str: The generated response.
        """
        # Use the current state of the history as context for generating a response
        response = self.generate_response(query, self.history)
        
        # Update the chat history with the current query and response
        self.history.append((query, response))
        
        return response

# Example usage
chatbot = Chatbot()
print(chatbot.respond_to_query("Hello, how are you?"))
print(chatbot.respond_to_query("What is the weather like today?"))
print(chatbot.respond_to_query("Thank you!"))
```

4
```python
class LanguageModel:
    def predict(self, input_text):
        # Placeholder prediction method
        return f"Mock response for: {input_text}"

class DocumentRetriever:
    def retrieve(self, query):
        # Placeholder document retrieval method
        return f"Mock document related to: {query}"

class ConversationMemory:
    def __init__(self):
        self.memory = []

    def add_to_memory(self, query, response):
        self.memory.append((query, response))

    def reset_memory(self):
        self.memory = []

    def get_memory(self):
        return self.memory

def setup_conversational_retrieval_chain():
    # Initialize the components of the retrieval chain
    language_model = LanguageModel()
    document_retriever = DocumentRetriever()
    conversation_memory = ConversationMemory()
    
    # For demonstration purposes, this function will just return a dictionary
    # representing the initialized components. In a real implementation,
    # these components would be integrated into a more complex retrieval system.
    retrieval_chain = {
        "language_model": language_model,
        "document_retriever": document_retriever,
        "conversation_memory": conversation_memory
    }
    
    return retrieval_chain

# Example usage
retrieval_chain = setup_conversational_retrieval_chain()
print(retrieval_chain)
```

5.
```python
class EnhancedChatbot(Chatbot):
    def __init__(self):
        super().__init__()
        # Use ConversationMemory from the previous task for managing chat history
        self.conversation_memory = ConversationMemory()

    def add_to_history(self, query, response):
        """
        Adds a new entry to the conversation history.
        
        Args:
            query (str): The user's query.
            response (str): The chatbot's response.
        """
        self.conversation_memory.add_to_memory(query, response)

    def reset_history(self):
        """
        Resets the conversation history, clearing all past interactions.
        """
        self.conversation_memory.reset_memory()

    def respond_to_query(self, query):
        """
        Override the method to incorporate conversation memory management.
        """
        # Generate a response considering the updated history
        response = super().generate_response(query, self.conversation_memory.get_memory())
        
        # Update the conversation history with the new interaction
        self.add_to_history(query, response)
        
        return response

# Example usage
enhanced_chatbot = EnhancedChatbot()
print(enhanced_chatbot.respond_to_query("Hello, how are you?"))
enhanced_chatbot.reset_history()
print(enhanced_chatbot.respond_to_query("Starting a new conversation."))
```

6.
```python
def embed_document(document_text):
    # Placeholder function to simulate document text embedding
    return sum(ord(char) for char in document_text) % 100  # Simple hash for demonstration

def split_document_into_chunks(document, chunk_size=100):
    # Splits document text into manageable chunks
    return [document[i:i+chunk_size] for i in range(0, len(document), chunk_size)]

def perform_semantic_search(query_embedding, vector_store):
    # Finds the most relevant document chunk based on embedding similarity (placeholder logic)
    similarities = [abs(query_embedding - chunk_embedding) for chunk_embedding in vector_store]
    return similarities.index(min(similarities))

def generate_answer_from_chunk(chunk):
    # Placeholder function to simulate answer generation from a selected document chunk
    return f"Based on your question, a relevant piece of information is: \"{chunk[:50]}...\""

# Main Q&A system logic
document = "This is a long document. " * 100  # Simulated document
chunks = split_document_into_chunks(document, 100)
vector_store = [embed_document(chunk) for chunk in chunks]

# Simulate a user question and its embedding
user_question = "What is this document about?"
question_embedding = embed_document(user_question)

# Find the most relevant chunk
relevant_chunk_index = perform_semantic_search(question_embedding, vector_store)
relevant_chunk = chunks[relevant_chunk_index]

# Generate an answer based on the most relevant chunk
answer = generate_answer_from_chunk(relevant_chunk)
print(answer)
```

7.
```python
def integrate_memory_with_retrieval_chain(retrieval_chain, user_query):
    """
    Integrates the conversational retrieval chain with a memory system to maintain context.

    Args:
        retrieval_chain (dict): A mock retrieval chain containing language model,
                                 document retriever, and conversation memory.
        user_query (str): User's query to process.
    """
    # Retrieve components from the retrieval chain
    conversation_memory = retrieval_chain["conversation_memory"]
    language_model = retrieval_chain["language_model"]
    document_retriever = retrieval_chain["document_retriever"]

    # Simulate using the document retriever to find relevant information
    relevant_info = document_retriever.retrieve(user_query)

    # Retrieve conversation history as context
    context = conversation_memory.get_memory()

    # Simulate generating a response with the language model using the query and context
    response = language_model.predict(f"Query: {user_query}, Context: {context}, Relevant Info: {relevant_info}")

    # Update conversation memory with the new interaction
    conversation_memory.add_to_memory(user_query, response)

    return response

# Using the retrieval chain from Task 4 with a dummy query for demonstration
dummy_query = "Tell me more about this document."
response = integrate_memory_with_retrieval_chain(retrieval_chain, dummy_query)
print("Generated Response:", response)
```

8.
```python
def chatbot_cli():
    enhanced_chatbot = EnhancedChatbot()  # Assuming EnhancedChatbot is the extended version from previous tasks

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
            print("Conversation history has been reset.")
        elif user_input == "exit":
            break
        else:
            print("Invalid option. Please try again.")

# To run the CLI, simply call the function (commented out to prevent execution in non-interactive environments)
# chatbot_cli()
```

