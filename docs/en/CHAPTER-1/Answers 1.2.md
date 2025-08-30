# Answers 1.2

## Theory
1. The key message components when working with GPT models are `role` and `content`. `role` (system/user/assistant) identifies the speaker and guides the model’s style or behavior; `content` holds the message text. Distinguishing roles is essential for a correct dialogue simulation and expected behavior.
2. `system` messages set instructions, context, and constraints (style, tone, rules). `user` messages are the user’s inputs (questions, instructions) that the model should answer. Clear role separation helps control the model effectively.
3. Example of `system` influence: “Reply in the style of a playful poet” — the model will follow that style.
4. Message order shapes context and influences answers: user turns are interpreted in light of earlier system instructions and the conversation history.
5. In the customer review classification example, the categories are “Positive”, “Negative”, and “Neutral”.
6. Classifying movie review sentiment is useful for aggregating viewer opinions. Possible categories: “Positive”, “Negative”, “Neutral”.
7. Classifying news topics helps manage content and recommendations. Possible categories: “Politics”, “Technology”, “Sports”, “Entertainment”.
8. Classifying customer requests speeds routing and increases satisfaction. Categories: “Billing”, “Support”, “Sales”, “General Question”.
9. In classification, the `user_message` should contain the text to be labeled; keep it clear and concise so the model has enough context for an accurate result.
10. Classifying social‑post tone helps with moderation (flagging inappropriate content) and marketing (analyzing audience engagement). Example tones: “Serious”, “Ironic”, “Inspiring”, “Irritated”.

