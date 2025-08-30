# Answers 2.4

## Theory
1. Purpose of embeddings: convert text into numeric vectors that preserve semantic meaning, enabling computers to “understand” text.
2. Semantic similarity: reflected in similar vectors for words/sentences with related meaning in a high‑dimensional space.
3. How embeddings are learned: trained on text corpora; word vectors depend on usage context (distributional semantics).
4. Embeddings in semantic search: allow retrieving relevant documents by meaning, even without exact keyword matches.
5. Matching documents and queries: a document embedding represents overall meaning; a query embedding captures user intent; comparing them reveals relevant matches.
6. Vector store: a database for embeddings optimized for fast nearest‑neighbor search.
7. Choosing a store: depends on data size, persistence requirements, and purpose (research, prototype, production).
8. Chroma for prototyping: convenient for small/in‑memory scenarios (fast), but limited in persistence and scaling.
9. Typical pipeline: split text → generate embeddings → index in a vector store → handle query → generate answer.
10. Splitting: improves granularity; matching happens at the level of meaningful fragments (chunks), not entire documents.
11. Embedding generation: transforms text into vectors suitable for computational comparison.
12. Indexing in the store: enables fast retrieval of semantically similar fragments.
13. Query handling: create a query embedding and search for similar fragments using metrics (cosine similarity, Euclidean distance, etc.).
14. Answer generation: uses the retrieved fragments together with the original query to produce a coherent answer.
15. Environment setup: install libraries, configure API keys, and set up for embeddings and the vector store.
16. Loading and splitting documents: critical for effective text management and higher‑quality retrieval.
17. Illustrating similarity: can be shown via dot product or cosine similarity.
18. Chroma specifics: mind the persistence directory, clearing stale data, and correct collection initialization.
19. Similarity search: finds the fragments most relevant to the query.
20. Typical failures and remediation: duplicates and irrelevant results can be addressed via filtering and careful pipeline tuning.

## Practice
1.
```python
def generate_embeddings(sentences):
    """
    Generate a simple placeholder embedding for each sentence based on its length.

    Args:
    - sentences (list of str): List of sentences to embed.

    Returns:
    - list of int: One embedding per sentence (the sentence length).
    """
    return [len(sentence) for sentence in sentences]

def cosine_similarity(vector_a, vector_b):
    """
    Compute cosine similarity between two vectors.

    Args:
    - vector_a (list of float): First vector.
    - vector_b (list of float): Second vector.

    Returns:
    - float: Cosine similarity between `vector_a` and `vector_b`.
    """
    dot_product = sum(a*b for a, b in zip(vector_a, vector_b))
    magnitude_a = sum(a**2 for a in vector_a) ** 0.5
    magnitude_b = sum(b**2 for b in vector_b) ** 0.5
    return dot_product / (magnitude_a * magnitude_b)

# Example usage:
sentences = ["Hello, world!", "This is a longer sentence.", "Short"]
embeddings = generate_embeddings(sentences)
print("Embeddings:", embeddings)

vector_a = [1, 2, 3]
vector_b = [2, 3, 4]
similarity = cosine_similarity(vector_a, vector_b)
print("Cosine similarity:", similarity)
```

2.
```python
def cosine_similarity(vector_a, vector_b):
    """Compute cosine similarity between two vectors."""
    dot_product = sum(a*b for a, b in zip(vector_a, vector_b))
    magnitude_a = sum(a**2 for a in vector_a) ** 0.5
    magnitude_b = sum(b**2 for b in vector_b) ** 0.5
    if magnitude_a == 0 or magnitude_b == 0:
        return 0  # Avoid division by zero
    return dot_product / (magnitude_a * magnitude_b)
```

3.
```python
class SimpleVectorStore:
    def __init__(self):
        self.vectors = []  # Initialize empty list to store vectors

    def add_vector(self, vector):
        """Add a vector to the store."""
        self.vectors.append(vector)

    def find_most_similar(self, query_vector):
        """Find and return the vector most similar to `query_vector`."""
        if not self.vectors:
            return None  # Return None if the store is empty
        similarities = [cosine_similarity(query_vector, vector) for vector in self.vectors]
        max_index = similarities.index(max(similarities))
        return self.vectors[max_index]
```

4.
```python
import sys

def split_text_into_chunks(text, chunk_size):
    """Split the given text into chunks of the specified size."""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def load_and_print_chunks(file_path, chunk_size):
    """Load text from a file, split it into chunks, and print each chunk."""
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            chunks = split_text_into_chunks(text, chunk_size)
            for i, chunk in enumerate(chunks, 1):
                print(f"Chunk {i}:\n{chunk}\n{'-'*50}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_path> <chunk_size>")
        sys.exit(1)
    file_path = sys.argv[1]
    chunk_size = int(sys.argv[2])
    load_and_print_chunks(file_path, chunk_size)
```

5.
```python
# Assume SimpleVectorStore and cosine_similarity are defined earlier.

def generate_query_embedding(query):
    """
    Generate a simple placeholder embedding for the query based on its length.
    In real scenarios, you would use a model for embeddings.
    """
    return [len(query)]

def query_processing(store, query):
    """
    Process a query: generate its embedding, find the most similar fragment in the
    vector store, and print it.
    """
    query_embedding = generate_query_embedding(query)
    most_similar = store.find_most_similar(query_embedding)
    if most_similar is not None:
        print("Most similar document fragment:", most_similar)
    else:
        print("No document fragments found.")
```

6.
```python
def remove_duplicates(document_chunks):
    """Remove duplicate document fragments by exact content match."""
    unique_chunks = []
    for chunk in document_chunks:
        if chunk not in unique_chunks:
            unique_chunks.append(chunk)
    return unique_chunks
```

7.
```python
# Initialize SimpleVectorStore for demonstration
store = SimpleVectorStore()

# Placeholder document fragments and their embeddings
document_chunks = ["Document chunk 1", "Document chunk 2", "Document chunk 3"]
# Simulate embeddings based on length
document_embeddings = [[len(chunk)] for chunk in document_chunks]

# Add generated document embeddings to the store
for embedding in document_embeddings:
    store.add_vector(embedding)

# Perform similarity search with a sample query
query = "Document"
query_embedding = generate_query_embedding(query)

# Find the most similar document fragments via cosine similarity
similarities = [(cosine_similarity(query_embedding, doc_embedding), idx) for idx, doc_embedding in enumerate(document_embeddings)]
similarities.sort(reverse=True)  # Sort by similarity descending
top_n_indices = [idx for _, idx in similarities[:3]]  # Indices of top‑3 fragments

# Print IDs or contents of the top‑3 most similar document fragments
print("Top‑3 most similar document fragments:")
for idx in top_n_indices:
    print(f"{idx + 1}: {document_chunks[idx]}")
```


8.
```python
def embed_and_store_documents(document_chunks):
    """
    Generate embeddings for each document fragment and store them in SimpleVectorStore.

    Args:
    - document_chunks (list of str): List of document fragments.

    Returns:
    - SimpleVectorStore: Vector store initialized with document embeddings.
    """
    store = SimpleVectorStore()
    for chunk in document_chunks:
        # Placeholder embedding based on fragment length
        embedding = [len(chunk)]
        store.add_vector(embedding)
    return store
```

9.
```python
import json

def save_vector_store(store, filepath):
    """
    Save the state of a SimpleVectorStore to the specified file.

    Args:
    - store (SimpleVectorStore): Vector store to save.
    - filepath (str): Path to the output file.
    """
    with open(filepath, 'w') as file:
        json.dump(store.vectors, file)

def load_vector_store(filepath):
    """
    Load a SimpleVectorStore from the specified file.

    Args:
    - filepath (str): Path to the input file.

    Returns:
    - SimpleVectorStore: Loaded vector store.
    """
    store = SimpleVectorStore()
    with open(filepath, 'r') as file:
        store.vectors = json.load(file)
    return store

def vector_store_persistence():
    """Demonstrate saving and loading the state of SimpleVectorStore."""
    store = SimpleVectorStore()  # Assume it is already populated
    filepath = 'vector_store.json'

    # Example of saving and loading
    save_vector_store(store, filepath)
    loaded_store = load_vector_store(filepath)
    print("Vector store loaded with vectors:", loaded_store.vectors)
```

10.
```python
def evaluate_search_accuracy(queries, expected_chunks):
    """
    Evaluate similarity‑search accuracy for a list of queries and expected results.

    Args:
    - queries (list of str): Query strings.
    - expected_chunks (list of str): Expected most similar document fragments for each query.

    Returns:
    - float: Retrieval accuracy (fraction of correctly found fragments).
    """
    correct = 0
    # Embed and store documents plus some extras to ensure uniqueness
    store = embed_and_store_documents(expected_chunks + list(set(expected_chunks) - set(queries)))

    for query, expected in zip(queries, expected_chunks):
        query_embedding = generate_query_embedding(query)
        most_similar = store.find_most_similar(query_embedding)
        # Assume expected_chunks map to embeddings by length in the same way
        if most_similar and most_similar == [len(expected)]:
            correct += 1

    accuracy = correct / len(queries)
    return accuracy

# Assume embed_and_store_documents, generate_query_embedding, and SimpleVectorStore
# are implemented as described above.
```
