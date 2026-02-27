"""
# Tool Use and Function Calling

**Tool Use**, also known as **Function Calling** or **Tooling**, is a fundamental capability for AI agents that allows them to interact with external systems, access real-time information, and perform actions beyond their inherent knowledge or reasoning abilities. By integrating tools, agents can overcome limitations such as knowledge cutoffs, lack of access to proprietary data, or inability to perform complex computations.

## 🧠 Concept

The core concept involves an LLM being able to:

1.  **Identify Intent**: Understand when a user's request or an internal thought requires the use of an external tool.
2.  **Select Tool**: Choose the most appropriate tool from a predefined set of available tools.
3.  **Formulate Arguments**: Extract necessary arguments from the conversation or context to call the selected tool.
4.  **Execute Tool**: Invoke the external tool with the formulated arguments.
5.  **Process Observation**: Incorporate the tool's output (observation) back into its context to continue reasoning or formulate a final response.

This process effectively extends the agent's capabilities, allowing it to act as an intelligent orchestrator of various functions and services.

## 📝 How it Works

Modern LLMs are often fine-tuned or designed to recognize when a function call is needed and to respond with a structured output (e.g., JSON) that specifies the tool to be called and its arguments. The agent's control flow then parses this output, executes the actual function, and feeds the result back to the LLM.

### Example Flow

-   **User Query**: "What's the current stock price of Google (GOOG)?"

-   **LLM (Internal Thought/Function Call Suggestion)**:
    ```json
    {
        "tool_name": "get_stock_price",
        "arguments": {
            "symbol": "GOOG"
        }
    }
    ```

-   **Agent (Execution Layer)**:
    -   Parses the LLM's output.
    -   Calls the `get_stock_price` function with `symbol="GOOG"`.
    -   Receives `{"price": "150.25", "currency": "USD"}` as output.

-   **LLM (Processes Observation)**:
    -   Receives the tool's output as an observation.
    -   Formulates a natural language response.

-   **Agent (Final Response)**: "The current stock price of Google (GOOG) is $150.25 USD."

## 💡 Benefits

-   **Access to Real-time Information**: Agents can fetch current data (weather, news, stock prices) that is not part of their training data.
-   **Execution of Actions**: Agents can perform actions in the real world (send emails, book appointments, control devices) through APIs.
-   **Complex Computations**: Offload mathematical calculations, data analysis, or code execution to specialized tools.
-   **Reduced Hallucinations**: Ground responses in factual, external data, leading to more accurate and reliable outputs.
-   **Modularity and Extensibility**: New tools can be added or updated without retraining the entire LLM, making agents highly adaptable.

## 📊 Tool Description Formats

Tools are typically described to the LLM using structured formats, allowing the model to understand their purpose, required parameters, and expected outputs. Common formats include:

-   **JSON Schema**: Widely used for defining the structure of tool inputs and outputs.
-   **OpenAPI/Swagger**: For describing RESTful APIs as tools.
-   **Natural Language Descriptions**: Simple, human-readable descriptions of what a tool does.

### Example Tool Description (Conceptual)

```python
def get_current_weather(location: str, unit: str = "fahrenheit") -> dict:
    """
    Get the current weather in a given location.

    Args:
        location (str): The city and state, e.g., "San Francisco, CA"
        unit (str): The unit of temperature. Can be "celsius" or "fahrenheit".
    """
    # ... actual implementation ...
    pass
```

This Python function, along with its docstring, can be converted into a format that the LLM can understand and use to generate function calls.

## 📚 Resources

-   [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
-   [LangChain Tools Documentation](https://python.langchain.com/docs/modules/agents/tools/)
-   [LlamaIndex Tools Documentation](https://docs.llamaindex.ai/en/stable/module_guides/tool_use.html)
-   [Google AI Function Calling](https://ai.google.dev/docs/function_calling)
"""
