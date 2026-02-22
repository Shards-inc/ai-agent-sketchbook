---
name: autonomous-researcher
description: Enables an AI agent to conduct deep-web research, synthesize information, and generate comprehensive reports. Use for: automated information gathering, literature reviews, market analysis, and report generation.
---

# Autonomous Researcher Skill

This skill empowers an AI agent to act as an **Autonomous Researcher**, capable of performing in-depth investigations across various online sources, synthesizing findings, and producing structured reports.

## Key Features

-   **Deep-Web Research**: Utilizes search tools and web browsing capabilities to gather information from a wide range of online resources.
-   **Information Synthesis**: Processes and consolidates disparate pieces of information into coherent and insightful summaries.
-   **Report Generation**: Structures research findings into comprehensive reports, often including executive summaries, key findings, and recommendations.
-   **Source Citation**: Automatically cites sources to ensure transparency and verifiability of information.

## Usage Instructions

To leverage this autonomous researcher skill, follow these steps:

1.  **Define Research Query**: Provide a clear and specific research question or topic.
2.  **Specify Output Format**: Indicate the desired structure and depth of the research report (e.g., executive summary, detailed analysis, bibliography).
3.  **Initiate Research**: The agent will autonomously search, browse, and synthesize information to generate the report.

## Example Implementation Sketch

```python
class AutonomousResearcherAgent:
    def __init__(self, search_tool, browser_tool, llm):
        self.search_tool = search_tool
        self.browser_tool = browser_tool
        self.llm = llm

    def conduct_research(self, topic, report_format):
        # Logic for searching, browsing, extracting, synthesizing, and generating report
        pass
```

## Resources

-   [Example of an Autonomous Research Agent Architecture](https://www.example.com/autonomous-researcher-architecture) (Placeholder - replace with actual resource)
