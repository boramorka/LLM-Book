# Answers 1.4

## Theory

1. Chain of Thought (CoT) breaks problem solving into sequential steps, improving accuracy and making the decision process understandable.
2. CoT transparency lets users see the model’s logic, strengthening trust.
3. In education, CoT mimics a tutor: guiding step by step and fostering critical thinking.
4. In customer support, CoT helps unpack complex requests and arrive at precise answers step by step, reducing agent load.
5. Inner Monologue hides intermediate reasoning and shows only the result — unlike CoT, where steps are visible to the user.
6. For sensitive information, Inner Monologue reduces the chance of accidentally revealing details.
7. In “guided learning”, Inner Monologue provides hints without “spoiling” the full solution.
8. Environment prep includes loading the OpenAI key and importing required Python libraries.
9. `get_response_for_queries` sends prompts to the API and returns the model’s answer, encapsulating the interaction.
10. CoT prompting guides the model through steps when a direct answer is non‑obvious or requires complex logic.
11. In support, the system/user prompt structure directs reasoning for detailed product answers.
12. With Inner Monologue, you can extract only the final part of the answer to keep the interface concise and clear.

## Practice

Task 1: CoT — Detailed product answer

1. Implement `detailed_product_info_cot(product_name, user_question)` that uses CoT to build a detailed, stepwise answer.
2. Steps:
   - Step 1: Identify the product in question.
   - Step 2: Collect key characteristics (type, features, benefits).
   - Step 3: Use the collected data to answer `user_question` clearly and logically.

Task 2: Inner Monologue — Concise summary

1. Implement `concise_product_summary_inner_monologue(product_name, user_question)` that uses Inner Monologue to produce a concise answer.
2. Steps:
   - Internal: perform the same steps as CoT, but do not expose intermediate reasoning.
   - Final: return only a brief, direct answer to `user_question`.
3. Compare the outputs of both functions and explain their appropriate use cases.

