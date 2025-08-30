# Answers 1.5

## Theory

1. Prompt chaining decomposes a complex task into sequential, interconnected steps (prompts), each solving a subtask. Unlike the “monolithic” approach, it simplifies and improves control.
2. Analogies: step‑by‑step cooking of a complex dish; modular development where each module contributes to the final result.
3. Workflow management in chaining means checkpointing state after each step and adapting the next step to results so far.
4. Resource savings: each step processes only what’s needed, reducing computation versus one long prompt.
5. Error reduction: focusing on a single subtask simplifies debugging and enables targeted improvements.
6. Dynamic information loading matters due to context limits; chaining injects relevant data as needed.
7. Core steps: task decomposition, state management, prompt design, data loading/pre‑processing, dynamic context injection.
8. Best practices: avoid unnecessary complexity, write clear prompts, manage external context, aim for efficiency, and test continuously.
9. The examples use `dotenv` and `openai` for configuration and API calls.
10. The system message defines structure and format, increasing precision and consistency.
11. The product database stores details; lookup functions by name or category support effective support answers.
12. Converting JSON strings to Python objects simplifies downstream processing in chains.
13. Formatting a user answer from data keeps interactions informative and relevant.
14. Chaining lets the system move from the initial request to troubleshooting, warranty, and recommendations — covering complex support scenarios.

## Practice

1. `retrieve_model_response` function:
    ```python
    from openai import OpenAI

    client = OpenAI()

    def retrieve_model_response(message_sequence, model="gpt-4o-mini", temperature=0, max_tokens=500):
        response = client.chat.completions.create(
            model=model,
            messages=message_sequence,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    ```

2. Extracting products/categories from a request:
    ```python
    system_instruction = """
    You will receive support requests. The request will be delimited by '####'.
    Output a Python list of objects, each representing a product or category mentioned in the request.
    """

    user_query = "#### Tell me about SmartX ProPhone and FotoSnap DSLR Camera, and also your televisions ####"

    message_sequence = [
        {'role': 'system', 'content': system_instruction},
        {'role': 'user', 'content': user_query},
    ]

    extracted_info = retrieve_model_response(message_sequence)
    print(extracted_info)
    ```

3. Product database helpers:
    ```python
    product_database = {
        "SmartX ProPhone": {
            "name": "SmartX ProPhone",
            "category": "Smartphones and Accessories",
        },
        "FotoSnap DSLR Camera": {
            "name": "FotoSnap DSLR Camera",
            "category": "Cameras & Photography",
        },
        "UltraView HD TV": {
            "name": "UltraView HD TV",
            "category": "Televisions",
        },
    }

    def get_product_details_by_name(product_name):
        return product_database.get(product_name, "Product not found.")

    def get_products_in_category(category_name):
        return [p for p in product_database.values() if p["category"] == category_name]

    print(get_product_details_by_name("SmartX ProPhone"))
    print(get_products_in_category("Smartphones and Accessories"))
    ```

4. JSON string to list:
    ```python
    import json

    def json_string_to_python_list(json_string):
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return None

    json_input = '[{"category": "Smartphones and Accessories", "products": ["SmartX ProPhone"]}]'
    python_list = json_string_to_python_list(json_input)
    print(python_list)
    ```

5. Generate a user‑facing answer:
    ```python
    def generate_response_from_data(product_data_list):
        if not product_data_list:
            return "We couldn't find products matching your request."

        response_string = ""
        for product_data in product_data_list:
            response_string += f"Product: {product_data['name']}\n"
            response_string += f"Category: {product_data['category']}\n\n"
        return response_string

    python_list = [{'category': 'Smartphones and Accessories', 'products': ['SmartX ProPhone']}]
    final_response = generate_response_from_data(python_list)
    print(final_response)
    ```

6. End‑to‑end support scenario: describe how the assistant handles an initial product inquiry, troubleshooting, a warranty question, and accessory recommendations using the functions above.
    ```python
    # 1) Initial product inquiry: extract entities and list details
    system_instruction_catalog = """
    You will receive support requests delimited by '####'.
    Return a Python list of objects: mentioned products/categories.
    """

    user_query_1 = "#### I'm interested in upgrading my smartphone. What can you tell me about the latest models? ####"

    message_sequence_1 = [
        {'role': 'system', 'content': system_instruction_catalog},
        {'role': 'user', 'content': user_query_1},
    ]
    extracted = retrieve_model_response(message_sequence_1)
    print("Extracted entities:", extracted)

    # Suppose we parsed 'extracted' to a Python list called parsed_entities (omitted for brevity)
    # You could then look up details via your product DB helpers:
    # for e in parsed_entities: ... get_product_details_by_name(...), get_products_in_category(...)

    # 2) Troubleshooting: step‑by‑step guidance for a specific product issue
    troubleshooting_query = "#### I just bought the FotoSnap DSLR Camera you recommended, but I can't pair it with my smartphone. What should I do? ####"
    system_instruction_troubleshooting = "Provide step‑by‑step troubleshooting advice for the customer’s issue."
    message_sequence_2 = [
        {'role': 'system', 'content': system_instruction_troubleshooting},
        {'role': 'user', 'content': troubleshooting_query},
    ]
    troubleshooting_response = retrieve_model_response(message_sequence_2)
    print("Troubleshooting response:\n", troubleshooting_response)

    # 3) Warranty: clarify coverage details
    follow_up_query = "#### Also, could you clarify what the warranty covers for the FotoSnap DSLR Camera? ####"
    system_instruction_warranty = "Provide detailed information about the product’s warranty coverage."
    message_sequence_3 = [
        {'role': 'system', 'content': system_instruction_warranty},
        {'role': 'user', 'content': follow_up_query},
    ]
    warranty_response = retrieve_model_response(message_sequence_3)
    print("Warranty response:\n", warranty_response)

    # 4) Recommendations: suggest compatible accessories based on user interest
    additional_assistance_query = "#### Given your interest in photography, would you like recommendations for lenses and tripods compatible with the FotoSnap DSLR Camera? ####"
    system_instruction_recommendations = "Suggest accessories that complement the user’s existing products."
    message_sequence_4 = [
        {'role': 'system', 'content': system_instruction_recommendations},
        {'role': 'user', 'content': additional_assistance_query},
    ]
    recommendations_response = retrieve_model_response(message_sequence_4)
    print("Accessory recommendations:\n", recommendations_response)
    ```

    This sequence demonstrates a complete, chained workflow where the assistant:
    - Extracts mentioned entities and consults a product database.
    - Provides step‑wise troubleshooting tailored to the problem.
    - Explains warranty coverage clearly and concisely.
    - Offers personalized accessory recommendations aligned with the user’s interests.
