---
name: basic-agent
description: Provides a foundational template for building AI agents using the ReAct pattern. Use for: quick prototyping of new agent ideas, understanding core agentic loops, and as a starting point for custom agent development.
---

# Basic Agent Skill

This skill provides a basic agent template, demonstrating the **ReAct** (Reasoning and Acting) pattern. It is designed to be a simple, yet effective, starting point for developing AI agents.

## Key Features

- **ReAct Loop**: Implements the fundamental Thought-Action-Observation cycle, enabling the agent to reason about its actions and learn from observations.
- **Tool Integration**: Offers a straightforward interface for incorporating custom tools, allowing the agent to interact with external systems or perform specific tasks.
- **Context Management**: Includes basic mechanisms for managing conversation history and maintaining context throughout interactions.

## Usage Instructions

To utilize this basic agent skill, follow these steps:

1.  **Define Tools**: Create Python functions that the agent can call to perform actions. These functions should be self-contained and clearly defined.
2.  **Initialize LLM**: Configure your preferred Large Language Model (LLM) to serve as the agent's reasoning engine.
3.  **Run Agent**: Instantiate the `BasicAgent` class with your LLM and tools, then invoke its `run` method with a user prompt to start the agent loop.

## Example Implementation Sketch

```python
class BasicAgent:
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools
        self.history = []

    def run(self, prompt):
        # The ReAct loop implementation goes here.
        # It involves: thinking, selecting a tool, executing the tool,
        # observing the result, and updating history.
        pass
```

## Resources

-   [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
