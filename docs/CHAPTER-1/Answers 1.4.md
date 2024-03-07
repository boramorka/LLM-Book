# Answers 1.4

## Theory

1. Chain of Thought Reasoning is a method that breaks down the problem-solving process into a sequence of logical steps, enhancing AI models' ability to navigate complex queries with greater precision. It boosts accuracy and demystifies the model's decision-making process.
2. The transparency of Chain of Thought Reasoning allows users to follow the AI's thought process behind its conclusions, similar to understanding a human expert's reasoning. This clarity and openness are key to building user trust in AI systems.
3. In educational tools, Chain of Thought Reasoning simulates the thought process of an expert tutor, guiding students through problems step by step. This approach encourages active learning, fosters deeper comprehension, and enhances critical thinking skills.
4. For customer service bots, Chain of Thought Reasoning improves understanding of complex queries and navigates a logical series of steps to provide accurate responses. This enhances customer satisfaction and efficiency by reducing the need for human intervention.
5. The Inner Monologue Technique involves the AI processing and considering steps internally without exposing the entire process to the user, showing only the final output or relevant aspects of the reasoning. This contrasts with Chain of Thought Reasoning by focusing on selective information presentation.
6. In sensitive information filtering, the Inner Monologue Technique ensures that AI models display only appropriate content by processing data internally. This protects user privacy and maintains information integrity.
7. For guided learning applications, the Inner Monologue Technique allows AI systems to provide hints or partial reasoning steps without revealing full solutions, challenging students and promoting deep engagement with material for a stronger understanding.
8. Setting up the environment involves loading the OpenAI API key and importing necessary Python libraries, preparing for executing reasoning tasks with AI models.
9. The `get_response_for_queries` function sends queries to the OpenAI API and retrieves model responses, encapsulating the logic for interacting with AI models based on structured prompts.
10. Chain-of-Thought prompting guides the AI model through a structured reasoning process, useful for complex queries where direct answers are not apparent, by outlining systematic steps for the model to follow.
11. In customer service, structuring system and user prompts guides AI models through reasoning processes to provide detailed product information, ensuring accurate and relevant responses to customer inquiries.
12. Extracting and presenting the final response in the Inner Monologue implementation involves selecting only the essential conclusion of the AI's processing, enhancing the user interface by providing clear and concise answers without overwhelming details.

## Practice
1.
```python
def chain_of_thought_prompting(user_query):
    # Define a delimiter for separating reasoning steps
    step_delimiter = "####"
    
    # System prompt guiding the model through the reasoning process
    system_prompt = f"""
Follow these steps to answer customer queries, using '{step_delimiter}' to delineate each step.

Step 1:{step_delimiter} Determine if the query pertains to a specific product rather than a general category.

Step 2:{step_delimiter} Identify if the product is among the listed items, including details such as brand, features, and price.

[Provide a list of products here]

Step 3:{step_delimiter} Assess any assumptions made by the customer regarding product comparisons or specifications.

Step 4:{step_delimiter} Verify the accuracy of these assumptions based on provided product information.

Step 5:{step_delimiter} Correct any misconceptions, referencing only the listed products, and respond in a courteous manner.
"""

    # Structuring the user query to fit the prompt format
    structured_user_query = f"{step_delimiter}{user_query}{step_delimiter}"

    # Return the system prompt and the structured user query
    return system_prompt, structured_user_query

# Example usage
user_query = "How does the BlueWave Chromebook compare to the TechPro Desktop in terms of cost?"
system_prompt, structured_user_query = chain_of_thought_prompting(user_query)

print("System Prompt:\n", system_prompt)
print("Structured User Query:\n", structured_user_query)
```

2.
```python
def get_final_response(model_output, delimiter):
    """
    Extracts only the final response from the model's output.

    Parameters:
    - model_output (str): The complete output from the model.
    - delimiter (str): The delimiter used to separate reasoning steps in the model's output.

    Returns:
    - str: The final response extracted from the model's output. In case of errors, returns a predefined error message.
    """
    try:
        # Split the model's output using the delimiter to separate reasoning steps
        # and select the last element as the final response.
        final_response = model_output.split(delimiter)[-1].strip()
        return final_response
    except Exception as error:
        # Handle any potential errors gracefully and return a predefined error message.
        return "Sorry, I'm unable to process the response at the moment. Please try again."

# Example usage
model_output = "#### Step 1: Analyzing the query.#### Step 2: Gathering relevant information.#### Final response: The BlueWave Chromebook is more cost-effective than the TechPro Desktop."
delimiter = "####"

final_response = get_final_response(model_output, delimiter)
print(final_response)
```

3.
```python
def get_response_for_queries(query_prompts, model_name="gpt-3.5-turbo", response_temperature=0, max_response_tokens=500):
    """
    Mock function to simulate retrieving responses from the OpenAI API.

    Parameters:
    - query_prompts: A list containing the system and user prompts.
    - model_name: Specifies the model version to use (ignored in mock).
    - response_temperature: Controls the randomness of the model's responses (ignored in mock).
    - max_response_tokens: Limits the length of the model's response (ignored in mock).

    Returns:
    A simulated model's response to the user's query.
    """
    # Example responses for demonstration purposes
    if "compare to the TechPro Desktop" in query_prompts[1]['content']:
        return "#### Step 1: Analyzing the query.#### Step 2: Gathering relevant information.#### Final response: The BlueWave Chromebook is more cost-effective than the TechPro Desktop."
    else:
        return "Televisions are currently not available for sale. We expect to restock next month."

# Example queries for Chain of Thought Reasoning and Inner Monologue Technique
chain_of_thought_query = [
    {'role': 'system', 'content': 'Your system prompt goes here.'},
    {'role': 'user', 'content': "How does the BlueWave Chromebook compare to the TechPro Desktop in terms of cost?"},
]

inner_monologue_query = [
    {'role': 'system', 'content': 'Your system prompt goes here.'},
    {'role': 'user', 'content': "Are televisions available for sale?"},
]

# Sending the queries and printing responses
response_cot = get_response_for_queries(chain_of_thought_query)
print("Chain of Thought Response:\n", response_cot)

response_im = get_response_for_queries(inner_monologue_query)
print("\nInner Monologue Response:\n", response_im)
```

4.
```python
def validate_response_structure(response, delimiter):
    """
    Validates if the response from the model correctly follows the structure defined by the Chain of Thought Reasoning steps.

    Parameters:
    - response (str): The model's response.
    - delimiter (str): The delimiter used to separate reasoning steps.

    Returns:
    - bool: True if the response adheres to the expected structure, False otherwise.
    """
    steps = response.split(delimiter)
    # Assuming a valid response must have at least 3 parts: initial analysis, reasoning, and final response
    return len(steps) >= 3

# Example usage
response = "#### Step 1: Analyzing the query.#### Step 2: Gathering relevant information.#### Final response: The BlueWave Chromebook is more cost-effective than the TechPro Desktop."
delimiter = "####"
print(validate_response_structure(response, delimiter))
```

5.
```python
import os
from dotenv import load_dotenv

class QueryProcessor:
    def __init__(self):
        self.api_key = None
        self.step_delimiter = "####"
    
    def load_api_key(self):
        """
        Loads the OpenAI API key from environment variables.
        """
        load_dotenv()  # Load environment variables from a .env file
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("API key is not set. Please check your environment variables.")
    
    def structure_prompt(self, user_query, technique='chain_of_thought'):
        """
        Structures the prompt based on the specified technique.
        """
        if technique == 'chain_of_thought':
            return self._chain_of_thought_prompt(user_query)
        elif technique == 'inner_monologue':
            return self._inner_monologue_prompt(user_query)
        else:
            raise ValueError("Unsupported technique specified.")
    
    def send_query(self, system_prompt, user_query):
        """
        Mocks sending a query to the OpenAI API and receiving a response.
        """
        try:
            # Here you would use openai.ChatCompletion.create() to send the query
            # For demonstration, we return a mock response
            if "compare" in user_query:
                return "#### Step 1: Analyzing the query.#### Step 2: Gathering relevant information.#### Final response: The BlueWave Chromebook is more cost-effective."
            else:
                return "Televisions are currently not available for sale."
        except Exception as e:
            # Handle errors such as network failures or API limits
            print(f"Failed to send query: {e}")
            return None

    def process_response(self, response, technique='chain_of_thought'):
        """
        Processes the response based on the specified technique.
        """
        if technique == 'chain_of_thought':
            return self._validate_response_structure(response)
        elif technique == 'inner_monologue':
            return response.split(self.step_delimiter)[-1].strip()
        else:
            raise ValueError("Unsupported technique specified.")
    
    def _chain_of_thought_prompt(self, user_query):
        """
        Private method to structure a prompt for Chain of Thought Reasoning.
        """
        # Define a system prompt for Chain of Thought Reasoning
        return f"{self.step_delimiter}{user_query}{self.step_delimiter}"

    def _inner_monologue_prompt(self, user_query):
        """
        Private method to structure a prompt for Inner Monologue Technique.
        """
        # For Inner Monologue, we might structure the prompt differently or use the same structure
        return f"{self.step_delimiter}{user_query}{self.step_delimiter}"

    def _validate_response_structure(self, response):
        """
        Validates if the response structure matches the expected format for Chain of Thought Reasoning.
        """
        steps = response.split(self.step_delimiter)
        return len(steps) >= 3

# Example usage
processor = QueryProcessor()
processor.load_api_key()  # Load the API key

# Chain of Thought Reasoning example
cot_prompt = processor.structure_prompt("How does the BlueWave Chromebook compare to the TechPro Desktop?", technique='chain_of_thought')
cot_response = processor.send_query(cot_prompt, "How does the BlueWave Chromebook compare to the TechPro Desktop?")
print("Chain of Thought Response Validation:", processor.process_response(cot_response, technique='chain_of_thought'))

# Inner Monologue example
im_prompt = processor.structure_prompt("Are televisions available for sale?", technique='inner_monologue')
im_response = processor.send_query(im_prompt, "Are televisions available for sale?")
print("Inner Monologue Final Response:", processor.process_response(im_response, technique='inner_monologue'))
```
