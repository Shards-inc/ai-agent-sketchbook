---
name: coding-assistant
description: Provides a specialized AI agent for code generation, debugging, refactoring, and code review. Use for: automating coding tasks, improving code quality, and accelerating software development workflows.
---

# Coding Assistant Skill

This skill provides a specialized AI agent designed to act as a **Coding Assistant**, capable of assisting with various software development tasks.

## Key Features

-   **Code Generation**: Generates code snippets, functions, or even entire modules based on natural language descriptions or specifications.
-   **Debugging**: Helps identify and suggest fixes for bugs in existing code, often by analyzing error messages and code logic.
-   **Code Refactoring**: Assists in improving the structure, readability, and maintainability of code without changing its external behavior.
-   **Code Review**: Provides automated feedback on code quality, adherence to coding standards, and potential areas for improvement.
-   **Language Agnostic**: Can be adapted to work with various programming languages.

## Usage Instructions

To utilize this coding assistant skill, follow these steps:

1.  **Specify Task**: Clearly describe the coding task (e.g., "generate a Python function to calculate Fibonacci sequence," "debug this JavaScript code," "refactor this class").
2.  **Provide Context**: Supply relevant code snippets, error messages, or design specifications.
3.  **Review Output**: Evaluate the generated code, suggested fixes, or refactoring proposals and integrate them as appropriate.

## Example Implementation Sketch

```python
class CodingAssistantAgent:
    def __init__(self, llm, code_executor=None, linter=None):
        self.llm = llm
        self.code_executor = code_executor # Optional: for running and testing code
        self.linter = linter # Optional: for static code analysis

    def assist_coding(self, task_description, code_context=None):
        # Logic for understanding the task, generating/modifying code,
        # and potentially using code_executor or linter for validation.
        pass
```

## Resources

-   [Best Practices for AI-Assisted Code Generation](https://www.example.com/ai-code-generation-best-practices) (Placeholder - replace with actual resource)
-   [Automated Code Refactoring Techniques](https://www.example.com/automated-refactoring) (Placeholder - replace with actual resource)
