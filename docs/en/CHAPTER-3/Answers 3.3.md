# Answers 3.3

## Theory
1. Setting up the environment for a quiz generator includes importing required libraries, suppressing non‑essential warnings, and loading API keys (CircleCI, GitHub, OpenAI).
2. The dataset structure should include a question template and a “quiz bank” organized by subjects, categories, and facts. For example: “History”, “Technology”, “Geography” with corresponding facts.
3. Prompt engineering guides the AI to generate content relevant to the selected category. The prompt template can prescribe selecting subjects from the bank and forming quiz questions.
4. LangChain’s role is to structure the prompt, choose the language model (LLM), and configure a parser for processing the output.
5. The quiz generation pipeline is a composition of a structured prompt, model, and parser, implemented using the LangChain Expression Language.
6. Functions such as `evaluate_quiz_content` are used to assess the relevance and correctness of generated quiz content by checking for expected keywords.
7. Proper refusal handling is tested via `evaluate_request_refusal`, which ensures the system returns the expected refusal for out‑of‑scope requests.
8. The “science” test checks that generated questions contain indicators of scientific topics (e.g., “physics”, “chemistry”, “biology”, “astronomy”).
9. The basic components of a CircleCI config for a Python project include: version, orbs, jobs (build/test), Docker image, steps (checkout/tests), and workflows.
10. Customizing the CircleCI configuration for a project involves setting the Python version, test commands, and adding extra steps to accurately reflect real build, test, and deployment processes.

## Practice
Solutions to the tasks:

### Task 1: Creating a quiz dataset

We define a Python dictionary representing a collection of quiz items, organized by subjects, each with its categories and facts.

```python
quiz_bank = {
    "Historical Conflict": {
        "categories": ["History", "Politics"],
        "facts": [
            "Began in 1914 and ended in 1918",
            "Involved two major alliances: the Allies and the Central Powers",
            "Known for the extensive use of trench warfare on the Western Front"
        ]
    },
    "Revolutionary Communication Technology": {
        "categories": ["Technology", "History"],
        "facts": [
            "Invented by Alexander Graham Bell in 1876",
            "Revolutionized long-distance communication",
            "First words transmitted were 'Mr. Watson, come here, I want to see you'"
        ]
    },
    "Iconic American Landmark": {
        "categories": ["Geography", "History"],
        "facts": [
            "Gifted to the United States by France in 1886",
            "Symbolizes freedom and democracy",
            "Located on Liberty Island in New York Harbor"
        ]
    }
}
```

### Task 2: Generating quiz questions using prompts

This function generates quiz questions based on a given category by referencing relevant subjects and facts from `quiz_bank`. It demonstrates string manipulation and formatting in Python to construct meaningful quiz questions.

```python
def generate_quiz_questions(category):
    # A list to store generated questions
    generated_questions = []

    # Iterate over each subject in the quiz bank
    for subject, details in quiz_bank.items():
        # Check whether the category appears in the subject’s categories
        if category in details["categories"]:
            # For each fact, create a question and add it to the list
            for fact in details["facts"]:
                question = f"What is described by the following fact: {fact}? Answer: {subject}."
                generated_questions.append(question)
    
    return generated_questions

# Example usage
history_questions = generate_quiz_questions("History")
for question in history_questions:
    print(question)
```

### Task 3: Implementing LangChain‑style prompt structuring

To simulate structuring a quiz prompt as it might be done with LangChain, we can define a Python function that formats a list of quiz questions into a structured prompt. This structured prompt imitates detailed instructions and formatting that would guide an LLM in generating or processing quiz content.

```python
def structure_quiz_prompt(quiz_questions):
    # Define a delimiter for separating questions
    section_delimiter = "####"
    
    # Start with an introductory instruction
    structured_prompt = "Instructions for generating a personalized quiz:\nEach question is separated by four hash symbols (####)\n\n"
    
    # Add each question, separated by the delimiter
    for question in quiz_questions:
        structured_prompt += f"{section_delimiter}\n{question}\n"
    
    return structured_prompt

# Example usage
quiz_questions = [
    "In which year was the Declaration of Independence signed?",
    "Who invented the telephone?"
]
print(structure_quiz_prompt(quiz_questions))
```

This function accepts a list of quiz questions and returns a single string that structures them to simulate input for a quiz‑generation LLM, using the specified delimiter to separate questions.

### Task 4: Quiz generation pipeline

```python
def generate_quiz_questions(category):
    """
    Simulates generating quiz questions based on a category.
    """
    # Placeholder for simple generation logic by category
    questions = {
        "Science": ["What is the chemical symbol for water?", "Which planet is known as the Red Planet?"],
        "History": ["Who was the first President of the United States?", "In what year did the Titanic sink?"]
    }
    return questions.get(category, [])

def structure_quiz_prompt(quiz_questions):
    """
    Structures a chat prompt with the provided quiz questions.
    """
    section_delimiter = "####"
    prompt = "Generated quiz questions:\n\n"
    for question in quiz_questions:
        prompt += f"{section_delimiter} Question: {question}\n"
    return prompt

def select_language_model():
    """
    Simulates selecting a language model.
    """
    # For this example, assume the model is a constant string
    return "gpt-3.5-turbo"

def execute_language_model(prompt):
    """
    Simulates executing the selected language model with the given prompt.
    """
    # Normally this would send the prompt to the model and receive output.
    # Here we simulate it by echoing the prompt with a confirmation.
    return f"The model received the following prompt: {prompt}\nModel: 'Questions created successfully.'"

def generate_quiz_pipeline(category):
    """
    Simulates creating and executing a quiz generation pipeline using placeholders.
    """
    # Step 1: Generate questions based on the chosen category
    quiz_questions = generate_quiz_questions(category)
    
    # Step 2: Structure the prompt with the generated questions
    prompt = structure_quiz_prompt(quiz_questions)
    
    # Step 3: Select the language model to simulate
    model_name = select_language_model()
    
    # Step 4: Execute the language model with the structured prompt
    model_output = execute_language_model(prompt)
    
    # Final: Return a message simulating pipeline execution
    return f"Pipeline executed using model: {model_name}. Output: {model_output}"

# Example usage
print(generate_quiz_pipeline("Science"))
```

This set of functions simulates a quiz generation pipeline: generating questions based on a category, structuring them into a prompt, selecting a model, and executing it to produce mock output.

### Task 5: Reusable quiz generation function

```python
def create_structured_prompt(system_prompt_message, user_question_template="{question}"):
    """
    Creates a structured prompt using a system message and a user question template.
    """
    prompt = (
        f"System instructions: {system_prompt_message}\n"
        f"User template: {user_question_template}\n"
    )
    return prompt

def select_language_model():
    """
    Simulates selecting a language model and temperature.
    """
    return "gpt-3.5-turbo", 0

def simulate_model_response(structured_prompt):
    """
    Simulates generating a response from the selected language model based on the structured prompt.
    """
    # Here the actual API call to the language model would occur
    # For simulation purposes we return a mock response
    return "A mock quiz has been generated based on the structured prompt."

def setup_output_parser(model_output):
    """
    Simulates configuring an output parser for formatting the model’s response.
    """
    # Simple formatting for demonstration
    formatted_output = f"Formatted quiz: {model_output}"
    return formatted_output

def generate_quiz_assistant_pipeline(system_prompt_message, user_question_template="{question}"):
    print("Creating a structured prompt with the system message and user question template...")
    structured_prompt = create_structured_prompt(system_prompt_message, user_question_template)
    
    print("Selecting language model: GPT-3.5-turbo with temperature 0")
    model_name, temperature = select_language_model()
    
    print("Simulating language model response...")
    model_output = simulate_model_response(structured_prompt)
    
    print("Configuring output parser to format responses")
    formatted_output = setup_output_parser(model_output)
    
    print("Assembling components into a quiz generation pipeline...")
    return formatted_output

# Example usage with a detailed system prompt
system_prompt_message = "Please generate a quiz based on the following categories: Science, History."
print(generate_quiz_assistant_pipeline(system_prompt_message))
```

These functions provide a basic simulation of the processes involved in structuring prompts for AI‑based quiz generation, assembling the pipeline to perform that generation, and creating a reusable function for generating quizzes with customizable parameters.

### Task 6: Evaluating generated quiz content

This function accepts generated quiz content and a list of expected keywords to ensure the output aligns with expected topics or subjects. It raises an assertion error if none of the expected keywords are present, indicating a mismatch between expected and generated content.

```python
def evaluate_quiz_content(generated_content, expected_keywords):
    # Check whether any expected keyword appears in the generated content
    if not any(keyword.lower() in generated_content.lower() for keyword in expected_keywords):
        raise AssertionError("The generated content does not contain any of the expected keywords.")
    else:
        print("The generated content successfully contains the expected keywords.")

# Example usage
generated_content = "The law of universal gravitation was formulated by Isaac Newton in the 17th century."
expected_keywords = ["gravity", "Newton", "physics"]
evaluate_quiz_content(generated_content, expected_keywords)
```

### Task 7: Handling invalid quiz requests

This function simulates evaluating the system’s response to an invalid quiz request. It verifies whether the generated refusal matches the expected refusal response, confirming correct handling of requests the system cannot fulfill.

```python
def evaluate_request_refusal(invalid_request, expected_response):
    # Simulate generating a response to an invalid request
    generated_response = f"Unable to generate a quiz for: {invalid_request}"  # Placeholder for an actual refusal response
    
    # Check whether the generated response matches the expected refusal response
    assert generated_response == expected_response, "The refusal response does not match the expected response."
    print("The refusal response correctly matches the expected response.")

# Example usage
invalid_request = "Generate a quiz about unicorns."
expected_response = "Unable to generate a quiz for: Generate a quiz about unicorns."
evaluate_request_refusal(invalid_request, expected_response)
```

### Task 8: Science quiz evaluation test

This function demonstrates using `evaluate_quiz_content` in a specific test scenario—checking that a generated science quiz includes questions related to expected science topics. It simulates generating quiz content and then evaluates it for science‑oriented keywords.

```python
def test_science_quiz():
    # Simulate generating quiz content
    generated_content = "The study of the natural world through observation and experiment is known as science. Key subjects include biology, chemistry, physics, and Earth sciences."
    
    # Define expected keywords or subjects for a science quiz
    expected_science_subjects = ["biology", "chemistry", "physics", "Earth sciences"]
    
    # Use evaluate_quiz_content to check for expected keywords
    try:
        evaluate_quiz_content(generated_content, expected_science_subjects)
        print("Science quiz content evaluation passed successfully.")
    except AssertionError as e:
        print(f"Science quiz content evaluation failed: {e}")

# Example usage
test_science_quiz()
```

Taken together, these functions provide mechanisms for evaluating the relevance and accuracy of generated quiz content, handling invalid requests appropriately, and running targeted tests to ensure quiz content meets specific educational or thematic criteria.

