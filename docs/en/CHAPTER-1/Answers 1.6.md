# Answers 1.6

## Theory

1. Evaluating LLM answers is necessary to understand effectiveness, alignment with goals, and areas to improve. Evaluate accuracy, relevance, and completeness.
2. Key metrics: accuracy, recall, F1, and user satisfaction ratings. These guide product development and release decisions.
3. The path to production is iterative: start with quick prototypes, find gaps, gradually increase complexity and dataset coverage. Practical value matters more than perfection.
4. High‑stakes scenarios (medicine, law, finance) require stricter validation, bias detection/mitigation, and ethical review.
5. Best practices: start small, iterate quickly, automate testing and quality checks.
6. Automated tests speed up gold‑standard comparisons, surface errors, and provide continuous feedback.
7. Choose metrics and rigor to match the application’s goals and risks; use heightened rigor for high stakes.
8. A full evaluation framework includes a rubric, protocols (who/what/how), and gold‑standard comparison when needed.
9. Advanced techniques: semantic similarity (embeddings), crowd evaluation, automated coherence/logic checks, and adaptive schemes tailored to the domain.
10. Continuous evaluation and diverse test cases increase reliability and relevance across scenarios.

## Practice (sketches)

1. Rubric‑based evaluation function:
    ```python
    def evaluate_response(response: str, rubric: dict) -> dict:
        results = {}
        total_weight = sum(rubric[c]['weight'] for c in rubric)
        total_score = 0
        for criteria, details in rubric.items():
            score = details.get('weight', 1)  # stub — replace with real logic
            feedback = f"Stub feedback for {criteria}."
            results[criteria] = {'score': score, 'feedback': feedback}
            total_score += score * details['weight']
        results['overall'] = {
            'weighted_average_score': total_score / total_weight,
            'feedback': 'Overall feedback based on the rubric.'
        }
        return results
    ```

2. Rubric template:
    ```python
    rubric = {
        'accuracy': {'weight': 3},
        'relevance': {'weight': 2},
        'completeness': {'weight': 3},
        'coherence': {'weight': 2},
    }
    ```

3. The ideal (gold) answer serves as a comparison point for weighted scoring and textual feedback.

