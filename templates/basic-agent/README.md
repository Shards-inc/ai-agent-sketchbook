# Basic Agent Template

This template provides a minimal implementation of an AI agent using the **ReAct** (Reasoning and Acting) pattern. It is designed for simplicity and serves as a foundation for more complex agentic workflows.

## 📋 Features

- **ReAct Loop**: Implements the Thought-Action-Observation cycle.
- **Tool Integration**: Simple interface for adding custom tools.
- **Context Management**: Basic handling of conversation history.

## 🚀 Getting Started

1. **Define Tools**: Create functions that the agent can call.
2. **Initialize LLM**: Configure your preferred language model.
3. **Run Agent**: Start the agent loop with a user prompt.

## 🛠️ Implementation Sketch

```python
class BasicAgent:
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools
        self.history = []

    def run(self, prompt):
        # Implementation of the ReAct loop
        pass
```

## 📚 Resources

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
