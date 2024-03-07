# Answers 2.5

## Theory
1. Maximum Marginal Relevance (MMR) is designed to optimize the balance between relevance and diversity in document retrieval. It selects documents that are both closely related to the query and dissimilar from one another, enhancing the breadth of information provided.
2. Self-query retrieval efficiently processes queries that involve both semantic content and specific metadata by splitting the query into semantic and metadata components, enabling precise and contextually relevant search results.
3. Contextual compression targets the extraction of the most relevant segments from documents, focusing on the essence of the information needed to answer a query, thereby improving the quality of responses and reducing unnecessary computational burden.
4. Setting up an environment involves loading necessary libraries, configuring access to APIs (such as OpenAI's API for embeddings), and initializing a vector database. This foundational step ensures that the system is equipped to perform advanced retrieval functions effectively.
5. Initializing a vector database involves embedding textual content into a high-dimensional space to facilitate efficient semantic similarity searches. This setup allows for rapid and accurate retrieval of documents based on their semantic closeness to a query.
6. Populating a vector database involves adding textual content and then using similarity search to find documents closely related to a query. Diverse search, enabled by MMR, further refines results to ensure a broad spectrum of information is covered.
7. Using MMR in document retrieval enhances diversity by preventing the clustering of similar documents in search results. This approach ensures a wider range of perspectives and information, making the retrieval process more informative and less redundant.
8. Metadata enhances search specificity by allowing for searches that go beyond semantic content, targeting specific document attributes (such as publication date or document type), resulting in more precise and relevant search outcomes.
9. Self-query retrievers automate the extraction of both semantic queries and relevant metadata from user inputs, simplifying the search process and making it more user-friendly, while ensuring that results are accurately tailored to the query's context.
10. Contextual compression improves retrieval efficiency by focusing on the most pertinent segments of documents, which not only streamlines the information presented to users but also conserves computational resources by reducing the data volume processed.
11. Best practices include a balanced application of MMR for diversity, effective use of metadata for specificity, optimization of contextual compression to balance information relevance and computational efficiency, and strategic preparation of documents for retrieval.
12. Vector-based methods are highly effective for semantic similarity searches but may lack specificity in certain contexts. Alternative methods like TF-IDF and SVM offer different advantages, such as better handling of specific keyword-based searches or categorization tasks.
13. The integration of advanced retrieval techniques significantly enhances semantic search systems by delivering more precise, diverse, and contextually relevant information, which improves the overall user experience in interacting with intelligent systems.
14. The ongoing development of NLP technologies promises further enhancements in retrieval techniques, potentially introducing more sophisticated methods for understanding and responding to complex queries, thereby maintaining the progression towards more intelligent and intuitive search capabilities.

## Practice

1. 
```python
from typing import List, Tuple
import numpy as np

# Placeholder for the OpenAI embedding function
def openai_embedding(text: str) -> List[float]:
    # This function would call the OpenAI API to get the embeddings for the text
    # For demonstration purposes, returning a random vector
    return np.random.rand(768).tolist()

# Placeholder similarity function that calculates the cosine similarity between two vectors
def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    # Convert lists to numpy arrays
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    # Calculate cosine similarity
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

class VectorDatabase:
    def __init__(self, persist_directory: str):
        self.persist_directory = persist_directory
        self.database = []  # This will store tuples of (text, embedding)

    def add_text(self, text: str):
        # Generate embedding for the text
        embedding = openai_embedding(text)
        # Store the text and its embedding in the database
        self.database.append((text, embedding))

    def similarity_search(self, query: str, k: int) -> List[str]:
        query_embedding = openai_embedding(query)
        # Calculate similarity scores for all documents in the database
        similarities = [(text, cosine_similarity(query_embedding, embedding)) for text, embedding in self.database]
        # Sort documents based on similarity scores in descending order
        sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
        # Return the top k most similar texts
        return [text for text, _ in sorted_similarities[:k]]

# Example usage
if __name__ == "__main__":
    # Initialize the vector database with a dummy directory path
    vector_db = VectorDatabase("path/to/persist/directory")
    
    # Add some texts to the database
    vector_db.add_text("The quick brown fox jumps over the lazy dog.")
    vector_db.add_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    vector_db.add_text("Python is a popular programming language for data science.")

    # Perform a similarity search
    query = "Programming in Python"
    similar_texts = vector_db.similarity_search(query, 2)
    print("Similarity Search Results:", similar_texts)
```

2. 
```python
def compress_segment(segment: str, query: str) -> str:
    # Placeholder for an external utility function that compresses a segment based on the query
    # This should return a shorter version of the segment that's relevant to the query
    return segment[:len(segment) // 2]  # Mock implementation

def compress_document(document: List[str], query: str) -> List[str]:
    compressed_document = [compress_segment(segment, query) for segment in document]
    return compressed_document

# Example usage of compress_document
document = [
    "The first chapter introduces the concepts of machine learning.",
    "Machine learning techniques are varied and serve different purposes.",
    "In the context of data analysis, regression models can predict continuous outcomes."
]
query = "machine learning"
compressed_doc = compress_document(document, query)
print("Compressed Document Segments:", compressed_doc)

```

3. 
```python
def similarity(doc_id: str, query: str) -> float:
    # Placeholder function to compute similarity between a document and a query
    return 0.5  # Mock implementation

def diversity(doc_id1: str, doc_id2: str) -> float:
    # Placeholder function to compute diversity between two documents
    return 0.5  # Mock implementation

def max_marginal_relevance(doc_ids: List[str], query: str, lambda_param: float, k: int) -> List[str]:
    selected = []
    remaining = doc_ids.copy()

    while len(selected) < k and remaining:
        mmr_scores = {doc_id: lambda_param * similarity(doc_id, query) - 
                      (1 - lambda_param) * max([diversity(doc_id, sel) for sel in selected] or [0])
                      for doc_id in remaining}
        next_selected = max(mmr_scores, key=mmr_scores.get)
        selected.append(next_selected)
        remaining.remove(next_selected)

    return selected

# Example usage of max_marginal_relevance
doc_ids = ["doc1", "doc2", "doc3"]
query = "data analysis"
selected_docs = max_marginal_relevance(doc_ids, query, 0.5, 2)
print("Selected Documents:", selected_docs)

```

4. 
```python
def initialize_vector_db():
    # Initialize vector database
    vector_db = VectorDatabase("path/to/persist/directory")
    
    # Define some example texts
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Python is a popular programming language for data science."
    ]
    
    # Populate the database with texts
    for text in texts:
        vector_db.add_text(text)
    
    # Perform a similarity search
    query = "data science"
    similar_texts = vector_db.similarity_search(query, 2)
    print("Similarity Search Results:", similar_texts)
    
    # For demonstration of diverse search, let's reuse similar_texts with a comment explaining the intention
    # In a real scenario, this would involve applying MMR or another diversity enhancing method
    # This is just to illustrate how one might call such a function after its implementation
    print("Diverse Search Results (simulated):", similar_texts)

# Run the demonstration
initialize_vector_db()

```
