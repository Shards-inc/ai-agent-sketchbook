
import os
from typing import List, Dict, Any

class MockLLM:
    """A mock Large Language Model for demonstration purposes."""
    def generate(self, prompt: str) -> str:
        if "tool_code" in prompt:
            # Simulate tool execution based on prompt
            if "get_current_weather" in prompt:
                return "Observation: {\"location\": \"San Francisco\", \"temperature\": \"72F\", \"conditions\": \"Sunny\"}"
            elif "search_web" in prompt:
                return "Observation: Search result for 'latest AI news': AI advancements continue at rapid pace."
            else:
                return "Observation: Tool execution simulated."
        elif "Thought" in prompt:
            # Simulate a thought process leading to an action or answer
            if "weather" in prompt.lower():
                return "Thought: I need to use the weather tool to get the current weather. Action: get_current_weather(location=\"San Francisco\")"
            elif "AI news" in prompt.lower():
                return "Thought: I need to search the web for the latest AI news. Action: search_web(query=\"latest AI news\")"
            else:
                return "Thought: I will provide a general answer. Final Answer: I am an AI assistant and can help with many tasks."
        else:
            return "Thought: I will provide a general answer. Final Answer: I am an AI assistant and can help with many tasks."

class MockTool:
    """A mock tool for demonstration purposes."""
    def __init__(self, name: str, description: str, func):
        self.name = name
        self.description = description
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

def get_current_weather(location: str) -> Dict[str, str]:
    """Gets the current weather for a given location."""
    print(f"Executing get_current_weather for {location}")
    return {"location": location, "temperature": "72F", "conditions": "Sunny"}

def search_web(query: str) -> str:
    """Searches the web for a given query."""
    print(f"Executing search_web for {query}")
    return f"Search result for '{query}': AI advancements continue at rapid pace."

class BasicAgent:
    """A basic AI agent implementing the ReAct pattern."""
    def __init__(self, llm: MockLLM, tools: List[MockTool]):
        self.llm = llm
        self.tools = {tool.name: tool for tool in tools}
        self.history: List[str] = []

    def _format_prompt(self, query: str) -> str:
        tool_descriptions = "\n".join([f"> {tool.name}: {tool.description}" for tool in self.tools.values()])
        return (
            f"You are an AI assistant. Answer the following question as best as you can.\n"
            f"You have access to the following tools:\n"
            f"{tool_descriptions}\n\n"
            f"Use the following format:\n"
            f"Question: the input question you must answer\n"
            f"Thought: you should always think about what to do\n"
            f"Action: the action to take, should be one of [{', '.join(self.tools.keys())}]\n"
            f"Action Input: the input to the action\n"
            f"Observation: the result of the action\n"
            f"... (this Thought/Action/Action Input/Observation can repeat N times)\n"
            f"Thought: I now know the final answer\n"
            f"Final Answer: the final answer to the original input question\n\n"
            f"Question: {query}\n"
            f"{'\n'.join(self.history)}"
        )

    def run(self, query: str) -> str:
        self.history = []
        max_iterations = 5
        for i in range(max_iterations):
            prompt = self._format_prompt(query)
            response = self.llm.generate(prompt)
            self.history.append(response)
            print(f"LLM Response ({i+1}): {response}")

            if "Final Answer:" in response:
                return response.split("Final Answer:")[-1].strip()

            try:
                thought_part = response.split("Thought:")[-1]
                action_line = next((line for line in thought_part.split('\n') if line.startswith("Action:")), None)
                action_input_line = next((line for line in thought_part.split('\n') if line.startswith("Action Input:")), None)

                if action_line and action_input_line:
                    action_name = action_line.split("Action:")[-1].strip()
                    action_input_str = action_input_line.split("Action Input:")[-1].strip()

                    if action_name in self.tools:
                        # Basic parsing for action input - assumes simple key=value or single argument
                        # This part would need more robust parsing for real-world scenarios
                        if '=' in action_input_str and '{' not in action_input_str:
                            key, value = action_input_str.split('=', 1)
                            action_input = {key.strip(): value.strip().strip('"')}
                        elif action_input_str.startswith('{') and action_input_str.endswith('}'):
                            import json
                            action_input = json.loads(action_input_str)
                        else:
                            action_input = action_input_str # Assume it's a single string argument

                        tool_output = self.tools[action_name](**action_input) if isinstance(action_input, dict) else self.tools[action_name](action_input)
                        self.history.append(f"Observation: {tool_output}")
                    else:
                        self.history.append(f"Observation: Unknown tool: {action_name}")
                else:
                    self.history.append("Observation: Could not parse Action or Action Input from LLM response.")
            except Exception as e:
                self.history.append(f"Observation: Error during tool parsing/execution: {e}")
                print(f"Error: {e}")

        return "Final Answer: I could not determine the answer within the given iterations."

if __name__ == "__main__":
    llm = MockLLM()
    weather_tool = MockTool("get_current_weather", "A tool to get the current weather for a location.", get_current_weather)
    search_tool = MockTool("search_web", "A tool to search the web for information.", search_web)

    agent = BasicAgent(llm, [weather_tool, search_tool])

    print("\n--- Running Basic Agent (Weather Query) ---")
    result_weather = agent.run("What's the weather like in San Francisco?")
    print(f"Agent Final Result: {result_weather}")

    print("\n--- Running Basic Agent (AI News Query) ---")
    result_news = agent.run("Tell me about the latest AI news.")
    print(f"Agent Final Result: {result_news}")

    print("\n--- Running Basic Agent (General Query) ---")
    result_general = agent.run("Hello, how are you?")
    print(f"Agent Final Result: {result_general}")
