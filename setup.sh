#!/bin/bash

# Simple Question-Answering Agent Setup Script

echo "Setting up Simple Question-Answering Agent..."

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file prompt
echo "Creating .env file..."
if [ ! -f .env ]; then
    echo "# Anthropic API Key (Get yours from: https://console.anthropic.com/)" > .env
    echo "ANTHROPIC_API_KEY=" >> .env
    echo ".env file created. Please edit it to add your Anthropic API key."
else
    echo ".env file already exists. Make sure it contains your Anthropic API key."
fi

echo ""
echo "Setup complete! To get started:"
echo "1. Edit the .env file and add your Anthropic API key"
echo "2. Run: source venv/bin/activate  # if not already activated"
echo "3. Run: python qa_agent.py"
echo "" 