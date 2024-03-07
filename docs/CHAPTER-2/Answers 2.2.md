# Answers 2.2

## Theory

1. Document loaders in LangChain are specialized components designed to facilitate the access and conversion of data from various formats and sources into a standardized document object. They play a crucial role in enabling seamless integration and processing of diverse data types (like PDFs, HTML, and JSON) within LangChain applications, particularly for data-driven applications with conversational interfaces and Large Language Models.

2. Unstructured data loaders are adept at handling data from public and proprietary sources such as YouTube, Twitter, Figma, and Notion, dealing with a broad spectrum of unstructured data. Structured data loaders, on the other hand, are tailored for applications involving tabular data, supporting sources like Airbyte, Stripe, and Airtable to enable semantic search and question-answering over structured datasets.

3. The process involves installing necessary packages, setting up API keys for services like OpenAI, and loading environment variables from a `.env` file. This setup ensures that the environment is correctly configured to interact with external data sources through LangChain document loaders.

4. The PyPDFLoader in LangChain loads PDF documents by initializing with the path to the PDF file and then loading the document pages. It facilitates the extraction, cleaning, and tokenization of text from PDFs, enabling further processing such as word frequency analysis and handling of special cases like blank pages.

5. Text cleaning and tokenization involve removing non-alphabetic characters and splitting the text into lowercase words for basic normalization. This process is crucial for preparing the text for analysis, improving the accuracy of operations like word frequency counts and enabling more effective data processing and insight extraction.

6. The process involves initializing a Generic Loader with the YouTube Audio Loader and Whisper Parser, loading the document, and then accessing the transcribed content. This setup allows for the transcription of YouTube videos into text, using OpenAI's Whisper model for accurate audio to text conversion.

7. Sentence tokenization breaks down the transcribed text into individual sentences, enabling detailed analysis or processing. Sentiment analysis, performed using tools like TextBlob, assesses the overall tone and subjectivity of the video content, providing insights into the emotional and subjective content of the transcriptions.

8. Web content is loaded using the WebBaseLoader, which takes a target URL as input and loads the content. The content is then processed using tools like BeautifulSoup to parse HTML, clean the web content by removing unwanted elements, and extract specific information like hyperlinks and headings.

9. The process involves cleaning the web content to improve readability and analysis potential, extracting specific information like hyperlinks and headings, and summarizing the content through sentence tokenization, stopword filtering, and word frequency analysis to provide a concise summary of the web content.

10. The NotionDirectoryLoader loads data from a Notion database exported as Markdown. It converts Markdown to HTML for easier parsing, extracts structured data like headings and links, organizes the data into a DataFrame for analysis, and allows for filtering and summarizing based on the content and metadata.

11. Best practices include optimizing API usage to avoid unexpected costs, preprocessing data after loading to ensure it is in a usable format for further analysis or model training, and contributing to open-source projects like LangChain by developing new loaders for unsupported data sources.

12. Contributing new document loaders to the LangChain project can expand its capabilities, enabling support for a wider range of data sources and formats. This not only benefits the broader community by providing more tools for data processing and analysis but also enhances the contributor's understanding and expertise in handling diverse data types.

## Practice

1.
```python
from langchain.document_loaders import PyPDFLoader
import re
from collections import Counter
import nltk

# Download the list of stopwords from NLTK
nltk.download('stopwords')
from nltk.corpus import stopwords

# Initialize the list of English stopwords
stop_words = set(stopwords.words('english'))

# Initialize the PDF Loader with the path to the PDF document
pdf_loader = PyPDFLoader("path/to/your/document.pdf")

# Load the document pages
document_pages = pdf_loader.load()

# Function to clean, tokenize, and remove stopwords from text
def clean_tokenize_and_remove_stopwords(text):
    words = re.findall(r'\b[a-z]+\b', text.lower())  # Tokenize and convert to lowercase
    filtered_words = [word for word in words if word not in stop_words]  # Remove stopwords
    return filtered_words

# Initialize a Counter object for word frequencies
word_frequencies = Counter()

# Iterate over each page in the document
for page in document_pages:
    if page.page_content.strip():  # Check if the page is not blank
        words = clean_tokenize_and_remove_stopwords(page.page_content)
        word_frequencies.update(words)

# Print the top 5 most common words not including stopwords
print("Top 5 most common words excluding stopwords:")
for word, freq in word_frequencies.most_common(5):
    print(f"{word}: {freq}")

```

2.
```python
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
import nltk

# Make sure nltk resources are downloaded (e.g., punkt for sentence tokenization)
nltk.download('punkt')
from nltk.tokenize import word_tokenize

def transcribe_youtube_video(video_url):
    # Directory where audio files will be saved temporarily
    audio_save_directory = "temp_audio/"
    
    try:
        # Initialize the loader with YouTube Audio Loader and Whisper Parser
        youtube_loader = GenericLoader(
            YoutubeAudioLoader([video_url], audio_save_directory),
            OpenAIWhisperParser()
        )

        # Load the document (transcription)
        youtube_documents = youtube_loader.load()

        # Access the transcribed content
        transcribed_text = youtube_documents[0].page_content

        # Tokenize the transcribed text and return the first 100 words
        first_100_words = ' '.join(word_tokenize(transcribed_text)[:100])
        return first_100_words
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
video_url = "https://www.youtube.com/watch?v=example_video_id"
print(transcribe_youtube_video(video_url))

```

3.
```python
import requests
from bs4 import BeautifulSoup

def load_and_clean_web_content(url):
    try:
        # Fetch the content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the status is 4xx, 5xx

        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get clean text by removing all HTML tags
        clean_text = soup.get_text(separator=' ', strip=True)

        # Print the cleaned text
        print(clean_text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred during parsing: {e}")

# Example usage
url = "https://example.com"
load_and_clean_web_content(url)

```

4.
```python
import markdown
from bs4 import BeautifulSoup
import os

def convert_md_to_html_and_extract_links(directory_path):
    # List all Markdown files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".md"):
            # Construct the full file path
            file_path = os.path.join(directory_path, filename)

            # Read the Markdown file
            with open(file_path, 'r', encoding='utf-8') as md_file:
                md_content = md_file.read()

            # Convert Markdown to HTML
            html_content = markdown.markdown(md_content)

            # Use BeautifulSoup to parse HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract and print all links
            links = soup.find_all('a', href=True)
            print(f"Links in {filename}:")
            for link in links:
                print(f"Text: {link.text}, Href: {link['href']}")
            print("------" * 10)  # Separator for clarity

# Example usage
directory_path = "path/to/your/notion/data"
convert_md_to_html_and_extract_links(directory_path)

```

5.
```python

```

6.
```python

```

7.
```python

```