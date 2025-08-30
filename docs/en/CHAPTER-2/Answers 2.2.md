# Answers 2.2

## Theory

1. Document loaders are LangChain components that extract data from various sources and formats, converting them into a unified document object (content + metadata). They are the basis for bringing PDFs, HTML, JSON, and more into LLM apps.
2. Unstructured loaders target sources like YouTube, Twitter, Figma, Notion, etc. Structured loaders target tabular/service sources (Airbyte, Stripe, Airtable), enabling semantic search and QA over tables.
3. Environment prep includes installing packages, configuring API keys (e.g., OpenAI), and loading environment variables from `.env`.
4. `PyPDFLoader` loads PDFs by path, letting you extract, clean, and tokenize text for downstream analysis (word frequencies, handling empty pages, etc.).
5. Cleaning and tokenization — removing noise, lowercasing, and splitting into words — are basic normalization steps for accurate counts and further processing.
6. For YouTube: `GenericLoader` + `YoutubeAudioLoader` + `OpenAIWhisperParser` download audio and transcribe it via Whisper.
7. Sentence tokenization enables more granular analysis. Sentiment analysis (e.g., with `TextBlob`) provides polarity/subjectivity information.
8. For web content, use `WebBaseLoader(url)` plus `BeautifulSoup` to strip markup and extract links/headings and other structure.
9. After cleaning, you can extract key information and build a concise summary based on stop‑word filtering and word frequencies.
10. `NotionDirectoryLoader` reads exported Notion data (Markdown), converts it to HTML for parsing, extracts structure (headings, links), and stores it in a DataFrame for filtering and summarizing.
11. Practical tips: optimize API calls to control cost, pre‑process right after loading, and consider contributing new loaders to LangChain.
12. Contributing new loaders expands the ecosystem, broadens supported sources, and builds contributor expertise.

## Practice

1.
```python
from langchain.document_loaders import PyPDFLoader
import re
from collections import Counter
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

pdf_loader = PyPDFLoader("path/to/your/document.pdf")
document_pages = pdf_loader.load()

def clean_tokenize_and_remove_stopwords(text):
    words = re.findall(r'\b[a-z]+\b', text.lower())
    return [w for w in words if w not in stop_words]

word_frequencies = Counter()
for page in document_pages:
    if page.page_content.strip():
        words = clean_tokenize_and_remove_stopwords(page.page_content)
        word_frequencies.update(words)

print("Top‑5 most frequent non‑stop words:")
for word, freq in word_frequencies.most_common(5):
    print(f"{word}: {freq}")
```

2.
```python
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
import nltk

nltk.download('punkt')
from nltk.tokenize import word_tokenize

def transcribe_youtube_video(video_url):
    audio_save_directory = "temp_audio/"
    try:
        youtube_loader = GenericLoader(
            YoutubeAudioLoader([video_url], audio_save_directory),
            OpenAIWhisperParser()
        )
        youtube_documents = youtube_loader.load()
        transcribed_text = youtube_documents[0].page_content
        first_100_words = ' '.join(word_tokenize(transcribed_text)[:100])
        return first_100_words
    except Exception as e:
        print(f"Error: {e}")
        return None

video_url = "https://www.youtube.com/watch?v=example_video_id"
print(transcribe_youtube_video(video_url))
```

3.
```python
import requests
from bs4 import BeautifulSoup

def load_and_clean_web_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        clean_text = soup.get_text(separator=' ', strip=True)
        print(clean_text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"Parsing error: {e}")

url = "https://example.com"
load_and_clean_web_content(url)
```

4.
```python
import markdown
from bs4 import BeautifulSoup
import os

def convert_md_to_html_and_extract_links(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".md"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as md_file:
                md_content = md_file.read()
            html_content = markdown.markdown(md_content)
            soup = BeautifulSoup(html_content, 'html.parser')
            links = soup.find_all('a', href=True)
            print(f"Links in {filename}:")
            for link in links:
                print(f"Text: {link.text}, Href: {link['href']}")
            print("------" * 10)

directory_path = "path/to/your/notion/data"
convert_md_to_html_and_extract_links(directory_path)
```

5.
```python
from textblob import TextBlob
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

def transcribe_and_analyze_sentiment(video_url):
    # Directory to temporarily store downloaded audio
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

        # Analyze sentiment with TextBlob
        blob = TextBlob(transcribed_text)
        polarity = blob.sentiment.polarity

        # Map polarity to a simple label
        if polarity > 0.1:
            sentiment_label = "positive"
        elif polarity < -0.1:
            sentiment_label = "negative"
        else:
            sentiment_label = "neutral"

        print(f"Polarity: {polarity:.3f}")
        print(f"Sentiment: {sentiment_label}")

        return transcribed_text, polarity, sentiment_label

    except Exception as e:
        print(f"Error: {e}")
        return None, None, None

# Example usage
video_url = "https://www.youtube.com/watch?v=example_video_id"
text, polarity, sentiment = transcribe_and_analyze_sentiment(video_url)
```


6.
```python
import pandas as pd
import os
import markdown
from bs4 import BeautifulSoup

def create_notion_dataframe_with_word_count(directory_path):
    documents_data = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".md"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as md_file:
                md_content = md_file.read()
            html_content = markdown.markdown(md_content)
            soup = BeautifulSoup(html_content, 'html.parser')
            clean_text = soup.get_text()
            word_count = len(clean_text.split())
            title = filename.replace('.md', '')
            for line in md_content.split('\n'):
                if line.strip().startswith('#'):
                    title = line.strip('#').strip()
                    break
            documents_data.append({
                'filename': filename,
                'title': title,
                'word_count': word_count,
                'content': clean_text[:100] + '...'
            })
    df = pd.DataFrame(documents_data)
    df_sorted = df.sort_values('word_count', ascending=False)
    print("Top 3 longest docs:")
    for _, row in df_sorted.head(3).iterrows():
        print(f"{row['title']} ({row['word_count']} words)")
    return df_sorted

directory_path = "path/to/your/notion/data"
df = create_notion_dataframe_with_word_count(directory_path)
print(df.head())
```

7.
```python
import requests
from bs4 import BeautifulSoup
import re

def load_and_summarize_web_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        for script in soup(["script", "style"]):
            script.decompose()
        clean_text = soup.get_text(separator=' ', strip=True)
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        sentences = [s.strip() for s in re.split(r'[.!?]+', clean_text) if s.strip()]
        if len(sentences) >= 2:
            summary = f"First: {sentences[0]}.\nLast: {sentences[-1]}."
        elif len(sentences) == 1:
            summary = f"Single sentence: {sentences[0]}."
        else:
            summary = "No sentences extracted."
        print("Simple summary:")
        print(summary)
        return summary
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except Exception as e:
        print(f"Parsing error: {e}")
        return None

url = "https://example.com"
summary = load_and_summarize_web_content(url)
```

