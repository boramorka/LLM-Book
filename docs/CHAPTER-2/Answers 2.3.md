# Answers 2.3

## Theory

1. The primary goal of document splitting in text processing is to create semantically meaningful chunks that facilitate efficient data retrieval and analysis, ensuring the data is organized in a way that is both manageable and analyzable for various applications.
2. Chunk size determines the length of each document chunk, which affects the granularity of the data analysis. A larger chunk size may retain more context but can be cumbersome for processing, while a smaller chunk size may lead to loss of context but can be more manageable for detailed analyses.
3. Chunk overlap is important because it ensures that critical information is not lost at the boundaries of chunks, maintaining context continuity between adjacent chunks. This overlap enables more coherent data retrieval and analysis by preventing the segmentation of closely related information.
4. The `CharacterTextSplitter` splits text based on a specific number of characters, suitable for straightforward chunking without a primary concern for semantic integrity. The `TokenTextSplitter`, on the other hand, divides text based on tokens, which is particularly useful for preparing data for LLMs with specific token limitations, thus ensuring that chunks align with the processing capabilities of the models.
5. A recursive character text splitter is more sophisticated than basic splitters as it recursively divides text based on a hierarchy of separators (e.g., paragraphs, sentences, words), allowing for nuanced splitting that maintains semantic coherence within chunks.
6. Lang Chain offers specialized splitters for code and markdown documents: the `Language Text Splitter`, which recognizes language-specific syntax and separators to appropriately segment code blocks, and the `Markdown Header Text Splitter`, which splits markdown documents based on header levels, adding header information to chunk metadata for enhanced context.
7. Setting up a development environment for document splitting involves importing necessary libraries, configuring API keys, ensuring all dependencies are correctly installed, and potentially appending paths to access custom modules. This setup ensures the environment is ready for efficient document processing.
8. The `RecursiveCharacterTextSplitter` is advantageous for its ability to maintain semantic integrity through nuanced splitting, adapting to the document's structure. Adjusting parameters like chunk size, chunk overlap, and recursion depth can optimize the splitter's performance for specific texts.
9. Splitting the alphabet string with different splitters illustrates operational differences by showing how a simple splitter might uniformly divide text, while a recursive splitter could consider semantic units within the text, resulting in chunks that better preserve the intended meaning or structure.
10. When deciding between character-based and token-based splitting techniques for LLMs, considerations include the model's token limit, the importance of semantic integrity, and the nature of the text being processed. Token-based splitting aligns chunks more closely with the model's processing capabilities, potentially improving analysis accuracy.
11. Markdown header text splitting preserves the logical organization of documents by splitting them based on header levels. This approach is important for document analysis as it ensures that the resulting chunks maintain the original structure and context, facilitating better understanding and navigation of the content.
12. Best practices for ensuring semantic coherence and optimal overlap management in document splitting include prioritizing strategies that maintain the text's meaning and context, experimenting with different overlap sizes to find a balance that prevents redundancy while preserving continuity, and enhancing chunk metadata to provide context.

## Practice
1.
```python
def split_by_char(text, chunk_size):
    """
    Splits the text into chunks of specified size.

    Parameters:
    - text (str): The text to be split.
    - chunk_size (int): The size of each chunk.

    Returns:
    - list: A list of text chunks.
    """
    chunks = []  # Initialize the list to hold the chunks
    for start_index in range(0, len(text), chunk_size):
        # Append the chunk to the list, which is a substring of the text starting
        # from start_index to start_index + chunk_size
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
    Splits the text into chunks of specified size.

    Parameters:
    - text (str): The text to be split.
    - chunk_size (int): The size of each chunk.

    Returns:
    - list: A list of text chunks.
    """
    chunks = []  # Initialize the list to hold the chunks
    for start_index in range(0, len(text), chunk_size):
        # Append the chunk to the list, which is a substring of the text starting
        # from start_index to start_index + chunk_size
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
        tokens = text.split()  # Split text into tokens based on spaces
        chunks = []
        start_index = 0

        while start_index < len(tokens):
            # Ensure that the end index does not exceed the length of tokens
            end_index = min(start_index + self.chunk_size, len(tokens))
            chunk = ' '.join(tokens[start_index:end_index])
            chunks.append(chunk)
            # Update start_index for the next chunk, considering the overlap
            start_index += self.chunk_size - self.chunk_overlap
            if self.chunk_overlap >= self.chunk_size:
                print("Warning: chunk_overlap should be less than chunk_size to avoid overlap issues.")
                break

        return chunks
```

4.
```python
def recursive_split(text, max_chunk_size, separators):
    if not separators:  # Base case: no more separators to try
        return [text]
    
    if len(text) <= max_chunk_size:  # If the current chunk is within the size limit
        return [text]
    
    # Try to split the text using the first separator
    separator = separators[0]
    parts = text.split(separator)
    
    if len(parts) == 1:  # If the text doesn't contain the separator, move to the next separator
        return recursive_split(text, max_chunk_size, separators[1:])
    
    chunks = []
    current_chunk = ""
    for part in parts:
        if len(current_chunk + part) > max_chunk_size and current_chunk:
            # If adding the current part exceeds max_chunk_size, save the current chunk and reset
            chunks.append(current_chunk.strip())
            current_chunk = part + separator
        else:
            # Otherwise, add the part to the current chunk
            current_chunk += part + separator
    
    # Make sure to add the last chunk if it's not empty
    if current_chunk.strip():
        chunks.extend(recursive_split(current_chunk.strip(), max_chunk_size, separators))
    
    # Flatten the list in case of nested lists resulting from recursive calls
    flat_chunks = []
    for chunk in chunks:
        if isinstance(chunk, list):
            flat_chunks.extend(chunk)
        else:
            flat_chunks.append(chunk)
    
    return flat_chunks
```

5.
To implement the `MarkdownHeaderTextSplitter` class as described, we need to follow these steps:

1. **Initialization**: The class initializer will store the header patterns to split on, along with their associated names or levels, for later use in the text splitting process.

2. **Text Splitting**: The `split_text` method will analyze the input markdown text, identify headers based on the specified patterns, and split the text into chunks. Each chunk will start with a header and include all subsequent text up to the next header of the same or higher priority.

Here's how the class could be implemented:

```python
import re

class MarkdownHeaderTextSplitter:
    def __init__(self, headers_to_split_on):
        self.headers_to_split_on = sorted(headers_to_split_on, key=lambda x: len(x[0]), reverse=True)
        self.header_regex = self._generate_header_regex()

    def _generate_header_regex(self):
        # Generate a regex pattern that matches any of the specified headers
        header_patterns = [re.escape(header[0]) for header in self.headers_to_split_on]
        combined_pattern = '|'.join(header_patterns)
        return re.compile(r'(' + combined_pattern + r')\s*(.*)')

    def split_text(self, markdown_text):
        chunks = []
        current_chunk = []
        lines = markdown_text.split('\n')
        
        for line in lines:
            # Check if the line starts with one of the specified headers
            match = self.header_regex.match(line)
            if match:
                # If we're already collecting a chunk, save it before starting a new one
                if current_chunk:
                    chunks.append('\n'.join(current_chunk).strip())
                    current_chunk = []

            # Add the current line to the chunk
            current_chunk.append(line)

        # Don't forget to add the last chunk
        if current_chunk:
            chunks.append('\n'.join(current_chunk).strip())

        return chunks

# Example usage:
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
    print(f"Chunk {i+1}:\n{chunk}\n---")
```

This implementation does the following:

- During initialization, it sorts the headers by their length in descending order to ensure that longer (and thus more specific) markdown header patterns are matched first. This is important because, in markdown, headers are differentiated by the number of `#` characters, and we want to match the most specific header possible.
- It compiles a regular expression that can match any of the specified header patterns at the start of a line.
- The `split_text` method goes through each line of the input `markdown_text`, checking for header matches. When it finds a header, it starts or ends a chunk as appropriate. This method ensures that each chunk includes its starting header and all subsequent text up until the next header of the same or higher level.
