---
name: multi-agent-orchestrator
description: Provides a framework for coordinating multiple specialized AI agents to achieve complex goals. Use for: managing workflows involving diverse agent capabilities, task decomposition, and collaborative problem-solving.
---

# Multi-Agent Orchestrator Skill

This skill offers a framework for orchestrating and coordinating **multiple specialized AI agents** to collaboratively achieve complex objectives that a single agent might struggle with.

## Key Features

-   **Task Decomposition**: Breaks down large, complex problems into smaller, manageable sub-tasks that can be assigned to individual agents.
-   **Agent Coordination**: Manages the communication and interaction between different agents, ensuring smooth workflow execution.
-   **Dynamic Routing**: Intelligently routes sub-tasks to the most appropriate specialized agent based on their capabilities.
-   **Progress Monitoring**: Tracks the progress of individual agents and the overall task, providing insights into the collaborative process.
-   **Conflict Resolution**: Includes mechanisms to identify and resolve potential conflicts or dependencies between agent actions.

## Usage Instructions

To utilize this multi-agent orchestrator skill, follow these steps:

1.  **Define Overall Goal**: Clearly articulate the high-level objective that requires multiple agents.
2.  **Identify Specialized Agents**: Determine the types of specialized agents needed and their respective capabilities.
3.  **Configure Workflow**: Design the workflow, specifying how tasks are decomposed, assigned, and how agents interact.
4.  **Initiate Orchestration**: The orchestrator will manage the execution, coordinating agents to achieve the goal.

## Example Implementation Sketch

```python
class MultiAgentOrchestrator:
    def __init__(self, agents, task_manager):
        self.agents = agents # A collection of specialized agents
        self.task_manager = task_manager # Manages task decomposition and assignment

    def orchestrate_task(self, complex_goal):
        # Logic for decomposing the goal, assigning tasks to agents,
        # monitoring progress, and synthesizing results.
        pass
```

## Resources

-   [Architectures for Multi-Agent Systems](https://www.example.com/multi-agent-architectures) (Placeholder - replace with actual resource)
-   [Task Decomposition Strategies in AI Agents](https://www.example.com/task-decomposition) (Placeholder - replace with actual resource)
