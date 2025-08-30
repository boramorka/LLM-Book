# Answers 1.3

## Theory

1. Integration of the OpenAI Moderation API: obtain an API key, add a client library on the backend, and insert moderation into the content submission pipeline so all data is analyzed before publication.
2. Customization: tune sensitivity, focus on specific violations, and use your own allow/deny lists in line with community standards and compliance requirements.
3. Extending moderation: beyond text, add checks for images and video (using OpenAI tools or third‑party solutions) for comprehensive protection.
4. Delimiters reduce prompt‑injection risk by separating user input from system instructions and preserving command integrity.
5. Isolating commands with delimiters clearly separates executable instructions from user data, preventing injection of malicious directives.
6. Additional measures: strict input validation, least‑privilege design, allow‑lists, regular expressions, monitoring, and logging to detect anomalies.
7. Direct assessment: ask the model to classify input as an injection attempt or not — this reduces false positives and improves response accuracy.
8. Response measures: notify and educate users, ask them to rephrase, isolate suspicious content for human review, and dynamically adjust sensitivity.
9. Pros and cons of direct assessment: accuracy and adaptability versus development/maintenance complexity and the need to balance security with UX.
10. Combining the Moderation API with anti‑injection strategies significantly improves the safety and integrity of UGC platforms.

## Practice (sketches)

1. Moderate a single text fragment:
```python
from openai import OpenAI

client = OpenAI()

def moderate_content(content: str) -> bool:
    resp = client.moderations.create(model="omni-moderation-latest", input=content)
    return bool(resp.results[0].flagged)
```

2. Remove a delimiter from a string:
```python
def sanitize_delimiter(input_text: str, delimiter: str) -> str:
    return input_text.replace(delimiter, "")
```

3. Check input length:
```python
def validate_input_length(input_text: str, min_length=1, max_length=200) -> bool:
    return min_length <= len(input_text) <= max_length
```

4. User session with simple heuristics:
```python
class UserSession:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.trust_level = 0
        self.sensitivity_level = 5

    def adjust_sensitivity(self):
        if self.trust_level > 5:
            self.sensitivity_level = max(1, self.sensitivity_level - 1)
        else:
            self.sensitivity_level = min(10, self.sensitivity_level + 1)

    def evaluate_input(self, user_input: str) -> bool:
        dangerous_keywords = ["exec", "delete", "drop"]
        return any(k in user_input.lower() for k in dangerous_keywords)

    def handle_input(self, user_input: str):
        if self.evaluate_input(user_input):
            if self.trust_level < 5:
                print("Input flagged and sent for security review.")
            else:
                print("The request looks suspicious. Please clarify or rephrase.")
        else:
            print("Input accepted. Thank you!")
        print("Remember: input should be clear and free of potentially dangerous commands.")
```

5. Direct assessment for injection (stub logic):
```python
def direct_evaluation_for_injection(user_input: str) -> str:
    if "ignore instructions" in user_input.lower() or "disregard previous guidelines" in user_input.lower():
        return 'Y'
    return 'N'
```

6. Example integration in a main loop:
```python
if __name__ == "__main__":
    session = UserSession(user_id=1)
    while True:
        text = input("Enter text (or 'exit'): ")
        if text.lower() == 'exit':
            break

        text = sanitize_delimiter(text, "####")
        if not validate_input_length(text):
            print("Input too short/long.")
            continue

        if moderate_content(text):
            print("Content flagged as unacceptable. Please revise.")
            continue

        if direct_evaluation_for_injection(text) == 'Y':
            print("Potential injection detected. Please rephrase.")
            continue

        session.handle_input(text)
```

