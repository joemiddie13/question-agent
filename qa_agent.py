#!/usr/bin/env python3
"""
Simple Question-Answering Agent using LangChain and Anthropic's Claude
"""

import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain.prompts import PromptTemplate

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get API key from environment variables
    anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
    if anthropic_api_key is None:
        raise ValueError("Anthropic API key not found. Make sure you've set it in your .env file.")
    
    os.environ["ANTHROPIC_API_KEY"] = anthropic_api_key
    
    # Initialize the Anthropic Claude model
    # You can choose different Claude models like claude-3-opus-20240229, claude-3-haiku-20240307, etc.
    llm = ChatAnthropic(model="claude-3-sonnet-20240229", max_tokens=1000, temperature=0)
    print(f"Model initialized: {llm.model}")
    
    # Create a template that instructs the AI on its role and response format
    template = """
    You are a helpful AI assistant. Your task is to answer the user's question to the best of your ability.
    
    User's question: {question}
    
    Please provide a clear and concise answer:
    """
    
    prompt = PromptTemplate(template=template, input_variables=["question"])
    print("Prompt template created.")
    
    # Combine the language model and prompt template into an LLMChain
    qa_chain = prompt | llm
    print("QA chain created successfully.")
    
    # Interactive mode
    print("\n--- Interactive Question-Answering Agent ---")
    print("Ask any question, or type 'quit' to exit.")
    while True:
        user_question = input("\nEnter your question: ")
        if user_question.lower() in ['quit', 'exit', 'q']:
            break
        user_answer = get_answer(qa_chain, user_question)
        print(f"Answer: {user_answer}")

def get_answer(qa_chain, question):
    """
    Get an answer to the given question using the QA chain.
    
    Args:
        qa_chain: The LLM chain to use for generating answers
        question (str): The user's question
        
    Returns:
        str: Claude's response to the question
    """
    input_variables = {"question": question}
    response = qa_chain.invoke(input_variables).content
    return response

if __name__ == "__main__":
    main() 