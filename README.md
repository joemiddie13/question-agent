# Simple Question-Answering Agent

This project implements a basic question-answering agent using LangChain and Anthropic's Claude model.

## Overview

The agent is designed to:
- Understand natural language questions
- Generate concise, informative answers 
- Provide a simple interactive interface

## Quick Setup

The easiest way to set up this project is using the provided setup script:

```bash
# Clone the repository (if you haven't already)
cd question-agent

# Run the setup script
./setup.sh

# Edit the .env file to add your Anthropic API key
# Then run the agent
python qa_agent.py
```

## Manual Setup Instructions

If you prefer to set up manually:

1. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Set up your environment variables**:
   - Create a `.env` file in the project directory
   - Add your Anthropic API key to the `.env` file:
     ```
     ANTHROPIC_API_KEY=your_anthropic_api_key_here
     ```

4. **Run the agent**:
   ```
   python qa_agent.py
   ```

## Using the Agent

When you run the agent:

1. It will first demonstrate capabilities with two example questions
2. Then it will enter interactive mode where you can type your own questions
3. Type 'quit' or 'exit' to stop the program

## Project Structure

- `qa_agent.py` - Main Python script with the question-answering agent implementation
- `requirements.txt` - List of Python dependencies
- `setup.sh` - Setup script to create virtual environment and prepare the project
- `.env` - Environment file for storing your API key (created by setup script)

## Customization

You can customize the agent by:

- Changing the Claude model (edit the `model` parameter in `qa_agent.py`)
- Modifying the prompt template to give different instructions
- Adjusting parameters like `max_tokens` and `temperature`

## Dependencies

- LangChain: For building the agent pipeline
- Anthropic: For accessing Claude language models
- python-dotenv: For loading environment variables 