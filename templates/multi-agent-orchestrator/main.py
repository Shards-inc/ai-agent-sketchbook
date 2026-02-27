
import os
from typing import List, Dict, Any, Callable
import time

class MockAgent:
    """A mock specialized agent for demonstration purposes."""
    def __init__(self, name: str, capabilities: List[str]):
        self.name = name
        self.capabilities = capabilities

    def perform_task(self, task: str, data: Any = None) -> Dict[str, Any]:
        print(f"  [36m{self.name}[0m: Performing task [35m'{task}'[0m with data: {data}")
        time.sleep(0.5)
        if "research" in task.lower() and "web" in self.capabilities:
            return {"agent": self.name, "task": task, "result": f"Research findings for '{task}': Data from web sources.", "status": "completed"}
        elif "code generation" in task.lower() and "coding" in self.capabilities:
            return {"agent": self.name, "task": task, "result": f"Generated code for '{task}': print('Hello, World!')", "status": "completed"}
        elif "data analysis" in task.lower() and "analysis" in self.capabilities:
            return {"agent": self.name, "task": task, "result": f"Analysis report for '{task}': Key insights derived.", "status": "completed"}
        else:
            return {"agent": self.name, "task": task, "result": f"Task '{task}' performed by {self.name}.", "status": "completed"}

class MultiAgentOrchestrator:
    """A framework for coordinating multiple specialized AI agents."""
    def __init__(self, agents: List[MockAgent]):
        self.agents = {agent.name: agent for agent in agents}
        self.task_queue: List[Dict[str, Any]] = []
        self.results: List[Dict[str, Any]] = []

    def add_task(self, task_description: str, required_capabilities: List[str], data: Any = None):
        self.task_queue.append({
            "description": task_description,
            "required_capabilities": required_capabilities,
            "data": data,
            "status": "pending"
        })
        print(f"[34mOrchestrator[0m: Added task: [35m'{task_description}'[0m")

    def _find_suitable_agent(self, required_capabilities: List[str]) -> MockAgent | None:
        for agent in self.agents.values():
            if all(cap in agent.capabilities for cap in required_capabilities):
                return agent
        return None

    def orchestrate_tasks(self):
        print("\n[34mOrchestrator[0m: Starting task orchestration...")
        while self.task_queue:
            current_task = self.task_queue.pop(0)
            task_description = current_task["description"]
            required_capabilities = current_task["required_capabilities"]
            task_data = current_task["data"]

            agent = self._find_suitable_agent(required_capabilities)
            if agent:
                print(f"[34mOrchestrator[0m: Assigning task [35m'{task_description}'[0m to [36m{agent.name}[0m")
                result = agent.perform_task(task_description, task_data)
                self.results.append(result)
            else:
                print(f"[31mOrchestrator Error[0m: No suitable agent found for task [35m'{task_description}'[0m with capabilities {required_capabilities}")
                self.results.append({"task": task_description, "status": "failed", "error": "No suitable agent"})
        print("[34mOrchestrator[0m: All tasks processed.")

        return self.results

if __name__ == "__main__":
    # Define specialized agents
    research_agent = MockAgent("ResearchAgent", ["web", "data gathering"])
    coding_agent = MockAgent("CodingAgent", ["coding", "code generation", "debugging"])
    analysis_agent = MockAgent("AnalysisAgent", ["data analysis", "reporting"])
    general_agent = MockAgent("GeneralAgent", ["general assistance"])

    orchestrator = MultiAgentOrchestrator([research_agent, coding_agent, analysis_agent, general_agent])

    # Add tasks to the orchestrator
    orchestrator.add_task("research latest AI trends", ["web", "data gathering"])
    orchestrator.add_task("generate Python script for data processing", ["coding", "code generation"], {"input_format": "csv", "output_format": "json"})
    orchestrator.add_task("analyze market data", ["data analysis"])
    orchestrator.add_task("write a summary of research findings", ["reporting"]) # This task might not find a perfect match, demonstrating flexibility
    orchestrator.add_task("debug a web application", ["coding", "debugging"])
    orchestrator.add_task("perform complex calculations", ["math", "advanced logic"]) # No agent with 'math' capability

    # Run the orchestration process
    final_results = orchestrator.orchestrate_tasks()

    print("\n--- Final Orchestration Results ---")
    for res in final_results:
        print(f"- Task: [35m{res['task']}[0m, Agent: [36m{res.get('agent', 'N/A')}[0m, Status: [32m{res['status']}[0m, Result: {res.get('result', res.get('error'))}")
