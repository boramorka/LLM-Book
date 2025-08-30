# Answers 2.5

## Theory
1. Maximum Marginal Relevance (MMR): balances relevance and diversity by selecting documents close to the query yet dissimilar to each other.
2. Self‑Query Retrieval: splits a query into semantic content and metadata constraints for precise content‑plus‑attribute retrieval.
3. Contextual compression: extracts only the most relevant segments from documents, reducing noise and improving answer quality.
4. Environment setup: install libraries, configure API access (for embeddings), and initialize a vector store — the foundation for advanced retrieval.
5. Vector stores: hold embeddings and power fast similarity search.
6. Populating the store: add texts and run similarity search; MMR helps eliminate redundancy.
7. Boosting diversity with MMR: reduces clustering of near‑duplicates and broadens coverage.
8. Metadata for specificity: attributes (e.g., date, type) improve precision and relevance.
9. Self‑Query Retriever: automatically extracts both semantic and metadata parts from user input.
10. Benefits of contextual compression: saves computation and focuses on the essential.
11. Best practices: tune MMR, leverage metadata wisely, configure compression carefully, and prepare documents thoroughly.
12. Combining methods: embedding‑based retrieval excels at meaning, while TF‑IDF or SVM can help for keyword or classification‑based scenarios.
13. Advantages of advanced techniques: improved precision, diversity, context, and overall UX.
14. NLP outlook: continued progress will yield even smarter handling of complex queries.

## Practical Tasks

1.
```python
from typing import List
import numpy as np

def openai_embedding(text: str) -> List[float]:
    # Placeholder: return a random vector instead of calling OpenAI.
    return np.random.rand(768).tolist()

def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    v1 = np.array(vec1); v2 = np.array(vec2)
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

class VectorDatabase:
    def __init__(self, persist_directory: str):
        self.persist_directory = persist_directory
        self.database = []  # (text, embedding)

    def add_text(self, text: str):
        self.database.append((text, openai_embedding(text)))

    def similarity_search(self, query: str, k: int) -> List[str]:
        q = openai_embedding(query)
        scored = [(t, cosine_similarity(q, e)) for t, e in self.database]
        return [t for t, _ in sorted(scored, key=lambda x: x[1], reverse=True)[:k]]

if __name__ == "__main__":
    db = VectorDatabase("path/to/persist")
    db.add_text("The quick brown fox jumps over the lazy dog.")
    db.add_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    db.add_text("Python is a popular programming language for data science.")
    print("Similarity results:", db.similarity_search("Programming in Python", 2))
```

2.
```python
def compress_segment(segment: str, query: str) -> str:
    # Placeholder: return half the segment.
    return segment[:len(segment)//2]

def compress_document(document: List[str], query: str) -> List[str]:
    return [compress_segment(s, query) for s in document]

doc = [
    "The first chapter introduces the concepts of machine learning.",
    "Machine learning techniques are varied and serve different purposes.",
    "In data analysis, regression models can predict continuous outcomes.",
]
print("Compressed:", compress_document(doc, "machine learning"))
```

3.
```python
def similarity(doc_id: str, query: str) -> float: return 0.5
def diversity(doc_id1: str, doc_id2: str) -> float: return 0.5

def max_marginal_relevance(doc_ids: List[str], query: str, lambda_param: float, k: int) -> List[str]:
    selected, remaining = [], doc_ids.copy()
    while len(selected) < k and remaining:
        scores = {
            d: lambda_param * similarity(d, query) - (1 - lambda_param) * max([diversity(d, s) for s in selected] or [0])
            for d in remaining
        }
        nxt = max(scores, key=scores.get)
        selected.append(nxt)
        remaining.remove(nxt)
    return selected

print(max_marginal_relevance(["d1","d2","d3"], "query", 0.7, 2))
```


4.
```python
def initialize_vector_db():
    # Initialize the vector DB using the VectorDatabase class defined above
    vector_db = VectorDatabase("path/to/persist/directory")

    # Sample texts to add
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Python is a popular programming language for data science."
    ]

    for text in texts:
        vector_db.add_text(text)

    # Similarity search
    query = "data science"
    similar_texts = vector_db.similarity_search(query, 2)
    print("Similarity search results:", similar_texts)

    # Placeholder for “diverse search” demonstration — call MMR or similar here in a real setup
    print("Diverse search (simulated):", similar_texts)

# Run the demonstration
initialize_vector_db()
```
