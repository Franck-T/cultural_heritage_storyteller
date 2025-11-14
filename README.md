# 🏺 Cultural Heritage Storyteller  
### An AI-Powered Multi-Agent System for Generating Authentic Cultural Narratives

The **Cultural Heritage Storyteller** is an intelligent, multi-agent storytelling engine designed to preserve, explore, and creatively retell cultural knowledge in the form of structured narratives, legends, oral history, and educational stories.  
It leverages custom tools, an orchestrated agent workflow (CrewAI-style), and a curated dataset to generate culturally grounded stories with accuracy, emotional depth, and contextual alignment.

This project demonstrates how AI can support cultural preservation and digital storytelling using modular LLM orchestration.


## 🌟 Features

### 🧠 **Multi-Agent Story Generation Pipeline**
The project uses an orchestrated system of agents defined in `crew.py` to collaborate on:

- Story framing  
- Cultural context retrieval  
- Style harmonization  
- Narrative generation  
- Final editing & formatting  

Each agent has a dedicated role and contributes to the final story.

### 📚 **Cultural Knowledge Grounding**
The system uses training data (stored in `.pkl` files) to guide the AI toward culturally relevant storytelling patterns.

Includes:
- `my_training_data.pkl`
- `training_data.pkl`

These help the agents:
- Understand cultural values  
- Maintain accuracy  
- Preserve narrative coherence  
- Avoid fictional distortions  

## 📁 Project Structure

```
cultural_heritage_storyteller/
│── data/ # Cultural sources / raw references
│── task_outputs/ # Generated stories
│── my_training_data.pkl # Cultural dataset for grounding
│── training_data.pkl # Additional training data
│── src/
│ └── cultural_heritage/
│ │── main.py # Entry point to run the storytelling pipeline
│ │── crew.py # Multi-agent orchestration and configuration
│ │── tools/
│ │ └── custom_tool.py # Custom retrieval & enrichment tools
│ └── config/ # Model & agent configuration files
│── tests/ # Unit tests
│── hello.py # Dev/test script
│── pyproject.toml # Project metadata + dependencies
│── uv.lock # Dependency lockfile
│── README.md # (This file)
```

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/cultural_heritage/config/agents.yaml` to define your agents
- Modify `src/cultural_heritage/config/tasks.yaml` to define your tasks
- Modify `src/cultural_heritage/crew.py` to add your own logic, tools and specific args
- Modify `src/cultural_heritage/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the cultural_heritage Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The cultural_heritage Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.


Let's create wonders together with the power and simplicity of crewAI.
