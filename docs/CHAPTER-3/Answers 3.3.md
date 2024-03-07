# Answers 3.4

## Theory
1. The necessary components for setting up the environment for an AI-powered quiz generator include importing necessary libraries, silencing warnings for cleaner output, and loading API tokens for third-party services such as CircleCI, GitHub, and OpenAI.
2. To structure a dataset for generating quiz questions, one should define a quiz question template and initialize a quiz bank with subjects, categories, and facts. For example, categories could include History, Technology, and Geography, with facts related to specific subjects like "Historical Conflict," "Revolutionary Communication Technology," and "Iconic American Landmark."
3. Prompt engineering influences the generation of customized quizzes by guiding the AI to produce content relevant to the user's chosen category. An example prompt template might include instructions for the AI to select subjects from a quiz bank that align with the chosen category and create quiz questions based on those subjects.
4. The role of Langchain in structuring prompts for processing by an AI model involves converting the detailed quiz generation prompt into a structured format, selecting the language model, and setting up an output parser to convert the AI's response into a readable format.
5. The quiz generation pipeline consists of connecting the structured prompt, language model, and output parser using Langchain's expression language to create a seamless process for generating quizzes.
6. Ensuring the relevance and accuracy of generated quiz content through evaluation functions involves using functions like `evaluate_quiz_content` to check that the generated quiz includes expected keywords related to a given topic, ensuring content validity.
7. A method for testing the system's ability to decline generating a quiz under certain conditions involves the `evaluate_request_refusal` function, which verifies the system responds with a specified refusal message when faced with requests outside its capabilities or scope.
8. Testing the AI-generated quiz questions for alignment with expected science topics or subjects can be achieved through a function that evaluates whether the generated content includes specific keywords or themes indicative of the science category, such as "physics," "chemistry," "biology," and "astronomy."
9. The basic components of a CircleCI configuration file for a Python project include specifying the version, using orbs for simplified configuration, defining jobs for building and testing, specifying the Docker image to use, outlining steps for tasks like checking out code and running tests, and setting up workflows to run these jobs.
10. The importance of customization in the CircleCI configuration file to match project-specific needs involves adjusting the Python version, replacing commands based on how tests are run in the project, and adding additional setup steps as necessary to accurately reflect the project's requirements for building, testing, and deployment.

## Practice
Here are solutions for the tasks:

### Task 1: Create Quiz Dataset

We'll define a Python dictionary that represents a collection of quiz questions, organizing it by subjects, each with its categories and facts.

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

### Task 2: Generate Quiz Questions Using Prompts

For this function, we'll generate quiz questions based on a given category by accessing relevant subjects and facts from the `quiz_bank`. This approach demonstrates how to manipulate and format strings in Python to construct meaningful quiz questions.

```python
def generate_quiz_questions(category):
    # List to store generated questions
    generated_questions = []

    # Iterate through each subject in the quiz bank
    for subject, details in quiz_bank.items():
        # Check if the category is in the subject's categories
        if category in details["categories"]:
            # For each fact, create a question and add it to the list
            for fact in details["facts"]:
                question = f"What is described by: {fact}? Answer: {subject}."
                generated_questions.append(question)
    
    return generated_questions

# Example usage
history_questions = generate_quiz_questions("History")
for question in history_questions:
    print(question)
```


### Task 3: Implement Langchain Prompt Structuring

To simulate the structuring of a quiz prompt as might be done using Langchain, we can define a Python function that formats a list of quiz questions into a structured prompt. This structured prompt is designed to mimic the detailed instructions and formatting that would guide an AI model in generating or processing quiz content.

```python
def structure_quiz_prompt(quiz_questions):
    # Define a delimiter for separating questions
    section_delimiter = "####"
    
    # Start with an introductory instruction
    structured_prompt = "Instructions for Generating a Customized Quiz:\nEach question is separated by four hashtags (####)\n\n"
    
    # Add each question, separated by the delimiter
    for question in quiz_questions:
        structured_prompt += f"{section_delimiter}\n{question}\n"
    
    return structured_prompt

# Example usage
quiz_questions = [
    "What year was the Declaration of Independence signed?",
    "Who invented the telephone?"
]
print(structure_quiz_prompt(quiz_questions))
```

This function takes a list of quiz questions and returns a single string that structures these questions in a way that simulates the input for a quiz generation AI model, using a specified delimiter to separate the questions.

### Task 4: Quiz Generation Pipeline
```python
def generate_quiz_questions(category):
    """
    Simulates the generation of quiz questions based on a category.
    """
    # Placeholder for a simple question generation logic based on category
    questions = {
        "Science": ["What is the chemical symbol for water?", "What planet is known as the Red Planet?"],
        "History": ["Who was the first President of the United States?", "In what year did the Titanic sink?"]
    }
    return questions.get(category, [])

def structure_quiz_prompt(quiz_questions):
    """
    Structures a chat prompt with the provided quiz questions.
    """
    section_delimiter = "####"
    prompt = "Generated Quiz Questions:\n\n"
    for question in quiz_questions:
        prompt += f"{section_delimiter} Question: {question}\n"
    return prompt

def select_language_model():
    """
    Simulates the selection of a language model.
    """
    # For the sake of this example, we'll assume the model is a constant string
    return "gpt-3.5-turbo"

def execute_language_model(prompt):
    """
    Simulates executing the selected language model with the given prompt.
    """
    # This function would typically send the prompt to the model and receive the output.
    # Here, we'll simulate this by echoing the prompt with a confirmation.
    return f"Model received the following prompt: {prompt}\nModel: 'Quiz questions structured successfully.'"

def format_model_output(model_output):
    """
    Formats the output from the language model.
    """
    # Simulate parsing and formatting model output for readability
    return f"Formatted model output:\n{model_output}"

def generate_quiz_pipeline(category="Science"):
    """
    Expanded quiz generation pipeline that simulates each step in the quiz generation process.
    """
    print("Setting up the quiz generation pipeline...")
    quiz_questions = generate_quiz_questions(category)
    print("Quiz questions generated based on category.")
    
    structured_prompt = structure_quiz_prompt(quiz_questions)
    print("Structuring the chat prompt with provided quiz questions...")
    
    model = select_language_model()
    print(f"Selected language model: {model}")
    
    model_output = execute_language_model(structured_prompt)
    print("Executing the language model with structured prompt...")
    
    formatted_output = format_model_output(model_output)
    print("Setting up the output parser for formatting the AI model's response...")
    
    print(formatted_output)
    print("Quiz generated successfully!")
    
# Example usage with a specified category
generate_quiz_pipeline("History")
```

### Task 5: Reusable Quiz Generation Function

This function simulates assembling the necessary components for generating quizzes, such as crafting a detailed system prompt based on provided parameters and simulating the selection of a language model and output parser.

```python
def create_structured_prompt(system_prompt_message, user_question_template):
    """
    Simulates creating a structured prompt combining system instructions and a user question template.
    """
    return f"{system_prompt_message}\n\nTemplate for Questions: {user_question_template}"

def select_language_model():
    """
    Simulates the selection of a language model with specific configurations.
    """
    # Placeholder for model selection
    model_name = "GPT-3.5-turbo"
    temperature = 0
    return model_name, temperature

def simulate_model_response(structured_prompt):
    """
    Simulates generating a response from the selected language model based on the structured prompt.
    """
    # This is where an actual API call to a language model would take place
    # For simulation purposes, we'll return a mock response
    return "Mock quiz generated based on the structured prompt."

def setup_output_parser(model_output):
    """
    Simulates setting up an output parser to format the model's response.
    """
    # Simple formatting for demonstration
    formatted_output = f"Formatted Quiz: {model_output}"
    return formatted_output

def generate_quiz_assistant_pipeline(system_prompt_message, user_question_template="{question}"):
    print("Creating structured prompt with system message and user question template...")
    structured_prompt = create_structured_prompt(system_prompt_message, user_question_template)
    
    print("Selecting language model: GPT-3.5-turbo with temperature 0")
    model_name, temperature = select_language_model()
    
    print("Simulating language model response...")
    model_output = simulate_model_response(structured_prompt)
    
    print("Setting up the output parser for formatting responses")
    formatted_output = setup_output_parser(model_output)
    
    print("Assembling components into a quiz generation pipeline...")
    return formatted_output

# Example usage with a detailed system prompt message
system_prompt_message = "Please generate a quiz based on the following categories: Science, History."
print(generate_quiz_assistant_pipeline(system_prompt_message))
```

These functions provide a basic simulation of the processes involved in structuring prompts for AI-driven quiz generation, assembling a pipeline for executing this generation, and crafting a reusable function for generating quizzes with customizable parameters.


### Task 6: Evaluate Generated Quiz Content

This function takes the generated quiz content and a list of expected keywords as inputs to ensure that the generated content aligns with the expected themes or subjects. It raises an assertion error if the content does not contain any of the expected keywords, indicating a mismatch between the expected and generated content.

```python
def evaluate_quiz_content(generated_content, expected_keywords):
    # Check if any of the expected keywords are in the generated content
    if not any(keyword.lower() in generated_content.lower() for keyword in expected_keywords):
        raise AssertionError("Generated content does not contain any of the expected keywords.")
    else:
        print("Generated content successfully contains expected keywords.")

# Example usage
generated_content = "The law of gravity was formulated by Isaac Newton in the 17th century."
expected_keywords = ["gravity", "Newton", "physics"]
evaluate_quiz_content(generated_content, expected_keywords)
```

### Task 7: Handle Invalid Quiz Requests

This function simulates the evaluation of the system's response to an invalid quiz request. It checks whether the generated refusal response matches an expected refusal response, asserting the correctness of the system's handling of requests that cannot be fulfilled.

```python
def evaluate_request_refusal(invalid_request, expected_response):
    # Simulate generating a response to the invalid request
    generated_response = f"Unable to generate a quiz for: {invalid_request}"  # Placeholder for an actual refusal response
    
    # Assert if the generated response matches the expected refusal response
    assert generated_response == expected_response, "The refusal response does not match the expected response."
    print("Refusal response correctly matches the expected response.")

# Example usage
invalid_request = "Generate a quiz about unicorns."
expected_response = "Unable to generate a quiz for: Generate a quiz about unicorns."
evaluate_request_refusal(invalid_request, expected_response)
```

### Task 8: Science Quiz Evaluation Test

This function demonstrates using the `evaluate_quiz_content` function within a specific test scenario—ensuring a generated science quiz includes questions related to expected scientific topics. It simulates generating quiz content and then evaluates it for the presence of science-related keywords.

```python
def test_science_quiz():
    # Simulate generating quiz content
    generated_content = "The study of the natural world through observation and experiment is known as science. Key subjects include biology, chemistry, physics, and earth science."
    
    # Define expected keywords or subjects for a science quiz
    expected_science_subjects = ["biology", "chemistry", "physics", "earth science"]
    
    # Use the evaluate_quiz_content function to check for the presence of expected keywords
    try:
        evaluate_quiz_content(generated_content, expected_science_subjects)
        print("Science quiz content evaluation passed.")
    except AssertionError as e:
        print(f"Science quiz content evaluation failed: {e}")

# Example usage
test_science_quiz()
```

These functions collectively provide mechanisms for evaluating the relevance and accuracy of generated quiz content, handling invalid requests appropriately, and conducting focused tests on quiz content to ensure it meets specific educational or thematic criteria.