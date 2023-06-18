import os                                                                       # Import the `os` module for working with environment variables
from dotenv import load_dotenv                                                  # Import the `load_dotenv` function from the `dotenv` module
import openai                                                                   # Import the `openai` module for using the OpenAI API

                                                                                # Load API key from .env file
load_dotenv()                                                                   # Load the environment variables from the .env file into the current session
openai.api_key = os.getenv('OpenAIKey')                                         # Assign the value of the 'OpenAIKey' environment variable as the OpenAI API key

def chat(prompt):
    """
    Function for generating a chat-based completion using the OpenAI API.

    Args:
        prompt (str): The user's message or prompt.

    Returns:
        str: The assistant's reply.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )                                                                           # Call the OpenAI API to generate a chat-based completion based on the provided prompt and messages

    reply = response['choices'][0]['message']['content']                        # Extract the assistant's reply from the API response
    return reply

                                                                                # Example usage
while True:
    user_input = input("User: ")                                                # Prompt the user for input
    response = chat(user_input)                                                 # Call the chat function to get the assistant's reply
    print("Assistant:", response)                                               # Print the assistant's reply
