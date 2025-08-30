# Answers 2.3

## Theory

1. The goal of splitting is to produce meaningful chunks for effective search and analysis.
2. Chunk size controls granularity: larger → more context; smaller → easier processing but risk losing cohesion.
3. Overlap preserves context at boundaries and prevents loss of important information.
4. `CharacterTextSplitter` splits by characters; `TokenTextSplitter` by tokens (handy for LLM limits).
5. The recursive splitter uses a hierarchy of separators (paragraphs/sentences/words) to preserve semantics.
6. Specialized splitters: `LanguageTextSplitter` for code (syntax‑aware) and `MarkdownHeaderTextSplitter` (heading levels, adds metadata).
7. Environment: libraries, keys, dependencies, imports — for robust processing.
8. `RecursiveCharacterTextSplitter` preserves semantics and adapts to structure; tune size/overlap/depth.
9. The “alphabet” demo highlights differences: even slicing vs. semantically aware splitting.
10. Characters vs. tokens depends on model limits, semantic needs, and text nature.
11. Splitting by Markdown headings preserves logical structure.
12. Best practices: keep meaning, tune overlap (avoid redundancy), enrich chunk metadata.

## Practical Tasks

1.
```python
def split_by_char(text, chunk_size):
    """
    Split text into chunks of a fixed size.

    Args:
    - text (str): The text to split.
    - chunk_size (int): The size of each chunk.

    Returns:
    - list[str]: List of string chunks.
    """
    chunks = []
    for start_index in range(0, len(text), chunk_size):
        chunks.append(text[start_index:start_index + chunk_size])
    return chunks

# Example usage
text = "This is a sample text for demonstration purposes."
chunk_size = 10

chunks = split_by_char(text, chunk_size)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")
```

2.
```python
def split_by_char(text, chunk_size):
    """
    Split text into chunks of a fixed size.

    Args:
    - text (str): The text to split.
    - chunk_size (int): The size of each chunk.

    Returns:
    - list: List of text chunks.
    """
    chunks = []  # Initialize an empty list to store chunks
    for start_index in range(0, len(text), chunk_size):
        # Append a chunk (substring) starting at start_index
        chunks.append(text[start_index:start_index + chunk_size])
    return chunks

# Example usage
text = "This is a sample text for demonstration purposes."
chunk_size = 10

chunks = split_by_char(text, chunk_size)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")
```

3.
```python
class TokenTextSplitter:
    def __init__(self, chunk_size, chunk_overlap=0):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text):
        tokens = text.split()  # Split text into tokens by spaces
        chunks = []
        start_index = 0

        while start_index < len(tokens):
            # Ensure end_index does not exceed total tokens length
            end_index = min(start_index + self.chunk_size, len(tokens))
            chunk = ' '.join(tokens[start_index:end_index])
            chunks.append(chunk)
            # Update start_index accounting for overlap
            start_index += self.chunk_size - self.chunk_overlap
            if self.chunk_overlap >= self.chunk_size:
                print("Warning: `chunk_overlap` should be less than `chunk_size` to avoid overlap issues.")
                break

        return chunks
```

# Example usage:

```python
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
markdown_text = """
# Header 1
This is some text under header 1.
## Header 2
This is some text under header 2.
### Header 3
This is some text under header 3.
"""

chunks = splitter.split_text(markdown_text)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:
{chunk}
---")
```

This implementation does the following:

- During initialization, it sorts header markers by length in descending order so that longer (more specific) Markdown headers match first. This matters because Markdown header levels differ by the number of `#` characters, and we want the most specific header matched.
- It compiles a regular expression that matches any of the specified header markers at the start of a line.
- The `split_text` method iterates over each line of the input Markdown, checking for header matches. When it finds a header, it appropriately starts or ends a chunk. Each chunk includes its starting header and all subsequent lines up to the next header of the same or higher priority.


4.
```python
def recursive_split(text, max_chunk_size, separators):
    if not separators:  # Base case: no separators left
        return [text]

    if len(text) <= max_chunk_size:  # Already within size
        return [text]

    # Try to split with the first separator
    separator = separators[0]
    parts = text.split(separator)

    if len(parts) == 1:  # Separator not found, try next
        return recursive_split(text, max_chunk_size, separators[1:])

    chunks = []
    current_chunk = ""
    for part in parts:
        # If adding the part would exceed the limit and we already have content, store current and start new
        if len(current_chunk + part) > max_chunk_size and current_chunk:
            chunks.append(current_chunk.strip())
            current_chunk = part + separator
        else:
            current_chunk += part + separator

    # Recurse on the remaining text to ensure size constraints
    if current_chunk.strip():
        chunks.extend(recursive_split(current_chunk.strip(), max_chunk_size, separators))

    # Flatten nested lists from recursion
    flat_chunks = []
    for chunk in chunks:
        if isinstance(chunk, list):
            flat_chunks.extend(chunk)
        else:
            flat_chunks.append(chunk)

    return flat_chunks
```

5.
To implement `MarkdownHeaderTextSplitter` as described, we follow these steps:

1. Initialization: store header patterns with their names/levels to use during splitting.
2. Text splitting: parse the input Markdown, identify headers by the given patterns, and split into chunks. Each chunk starts with a header and includes the following lines up to the next header of the same or higher priority.

```python
import re

class MarkdownHeaderTextSplitter:
    def __init__(self, headers_to_split_on):
        # Sort headers by marker length (longer first) for correct matching
        self.headers_to_split_on = sorted(headers_to_split_on, key=lambda x: len(x[0]), reverse=True)
        self.header_regex = self._generate_header_regex()

    def _generate_header_regex(self):
        # Build a regex matching any of the specified header markers
        header_patterns = [re.escape(header[0]) for header in self.headers_to_split_on]
        combined_pattern = '|'.join(header_patterns)
        return re.compile(r'(' + combined_pattern + r')\s*(.*)')

    def split_text(self, markdown_text):
        chunks = []
        current_chunk = []
        lines = markdown_text.split('
')

        for line in lines:
            # Check if the line starts with one of the header markers
            match = self.header_regex.match(line)
            if match:
                # If we already collected lines, store the previous chunk
                if current_chunk:
                    chunks.append('
'.join(current_chunk).strip())
                    current_chunk = []
                current_chunk.append(line)
            else:
                current_chunk.append(line)

        # Append the last collected chunk if present
        if current_chunk:
            chunks.append('
'.join(current_chunk).strip())

        return chunks
```

# Example usage:

```python
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
markdown_text = """
# Header 1
This is some text under header 1.
## Header 2
This is some text under header 2.
### Header 3
This is some text under header 3.
"""

chunks = splitter.split_text(markdown_text)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:
{chunk}
---")
```

This implementation does the following:

- During initialization, it sorts header markers by length in descending order so that longer (more specific) Markdown headers match first. This matters because Markdown header levels differ by the number of `#` characters, and we want the most specific header matched.
- It compiles a regular expression that matches any of the specified header markers at the start of a line.
- The `split_text` method iterates over each line of the input Markdown, checking for header matches. When it finds a header, it appropriately starts or ends a chunk. Each chunk includes its starting header and all subsequent lines up to the next header of the same or higher priority.

