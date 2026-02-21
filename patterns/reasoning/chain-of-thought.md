# Chain-of-Thought (CoT) Reasoning

**Chain-of-Thought (CoT)** is a prompting technique that encourages the model to generate a series of intermediate reasoning steps before arriving at a final answer.

## 🧠 Concept

By breaking down a complex problem into smaller, logical steps, CoT significantly improves the performance of LLMs on tasks involving arithmetic, commonsense reasoning, and symbolic manipulation.

## 🛠️ Implementation

### Zero-Shot CoT
Simply appending "Let's think step by step" to the prompt.

### Few-Shot CoT
Providing examples of (input, reasoning chain, output) triplets in the prompt.

## 📈 Benefits

- **Transparency**: Makes the model's reasoning process visible.
- **Accuracy**: Reduces errors in multi-step logical problems.
- **Debugging**: Easier to identify where the reasoning went wrong.

## 📚 Resources

- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)
