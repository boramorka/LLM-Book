# Answers 1.1

## Theory

1. Key benefits of integrating the OpenAI API: generating natural text, automating support, improving content creation, and expanding application functionality with advanced AI — boosting user engagement and operational efficiency.
2. Obtaining and securing the API key: register on the OpenAI platform, select a plan, and get your key in the dashboard. Store the key in environment variables or a secrets manager; never commit it to a repository — this prevents unauthorized access and potential losses.
3. `temperature`: controls creativity and variability of generated text. Low values make responses more predictable; higher values increase diversity. Choose based on the task.
4. Keys should be stored outside code (env vars or secret managers) to avoid leaks through source code and version control systems (VCS).
5. Model choice influences quality, speed, and cost. Balance model capability and resources to fit your app’s requirements.
6. Response metadata (e.g., token counts in `usage`) helps optimize prompts, manage costs, and use the API more efficiently.
7. An interactive interface includes dialogue history, input widgets, a send button, and panels to display responses. It updates in real time as answers arrive.
8. Best practices: post‑processing (style and grammar), personalization to user context, collecting feedback, and monitoring performance and spend.
9. Pitfalls: over‑trusting model output without checks. Use validation, a mix of automated and manual review, monitoring, and fine‑tuning.
10. Ethics and privacy: comply with data regulations, be transparent about AI’s role, implement review/correction processes, and consider social impact.

## Practice

Below is a progression of Python scripts for the OpenAI API — from a basic request to error handling and a CLI.

### Task 1: Basic API request

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What is the future of AI?"}],
    max_tokens=100,
)

print(response.choices[0].message.content)
```

### Task 2: Secure key handling

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What is the future of AI?"}],
    max_tokens=100,
)

print(response.choices[0].message.content)
```

### Task 3: Interpreting the response

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What is the future of AI?"}],
    max_tokens=100,
)

print("Response:", response.choices[0].message.content.strip())
print("Model used:", response.model)
print("Finish reason:", response.choices[0].finish_reason)
```

### Task 4: Error handling

```python
import os
from openai import OpenAI
from openai import APIConnectionError, RateLimitError, APIStatusError

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "What is the future of AI?"}],
        max_tokens=100,
    )
    print("Response:", response.choices[0].message.content.strip())
    print("Model used:", response.model)
    print("Finish reason:", response.choices[0].finish_reason)
except RateLimitError as e:
    print(f"Rate limit exceeded: {e}")
except APIConnectionError as e:
    print(f"Connection error: {e}")
except APIStatusError as e:
    print(f"API returned an error: {e}")
except Exception as e:
    print(f"Other error occurred: {e}")
```

### Task 5: CLI chat without post‑processing

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_openai():
    print("Starting chat with OpenAI. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": user_input}],
                max_tokens=100,
            )
            print("OpenAI:", response.choices[0].message.content.strip())
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_with_openai()
```

### Task 6: Post‑processing

```python
from openai import OpenAI
import os
from textblob import TextBlob

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def post_process_response(response_text):
    blob = TextBlob(response_text)
    corrected_text = str(blob.correct())
    formatted_text = " ".join(corrected_text.split())
    return formatted_text

def chat_with_openai():
    print("Starting chat with OpenAI. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": user_input}],
                max_tokens=100,
            )
            processed = post_process_response(response.choices[0].message.content)
            print("OpenAI:", processed)
        except Exception as e:
            print(f"Other error occurred: {e}")

if __name__ == "__main__":
    chat_with_openai()
```

### Tasks 7–8 (ideas)

- Generate a post outline for a user‑provided topic and output a bulleted list.
- Log response time and token usage for each call to a file for later analysis and optimization.

