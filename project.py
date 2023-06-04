import os
import openai
import sys

from dotenv import load_dotenv
from gpt import Prompt
from functions import *

# load values from the .env file if it exists
load_dotenv()

# configure OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    help()
    while True:
        try:
            i = input("What would you like to do? ")
            match i.lower():
                case "/translate" | "/t" | "translate" | "t":
                    print(
                        """
Welcome to CLI Bot Translation! 
          
Instructions for use:
1. Write the desired output language in the terminal as prompted in the command line
2. Write the text that you wish to translate (the bot will automatically detect the language that you wrote in)
3. Wait for the output to print on the command line

To terminate the programme, use ctrl + z
To return to the commands menu, use ctrl + c 
"""
                    )
                    while True:
                        try:
                            translate()
                        except KeyboardInterrupt:
                            print("")
                            break
                case "/chat" | "/c" | "chat" | "c":
                    print(
                        """
Welcome to CLI Bot Chatbot! 
          
Instructions for use:
1. Ask the bot anything and wait for response!
2. If your output is too long, it might take a longer time to generate the output or might even encounter errors in fetching the API response -> fix: try to ask shorter questions instead

To terminate the programme, use ctrl + z
To return to the commands menu, use ctrl + c 
"""
                    )
                    try:
                        chat()
                    except openai.error.APIError:
                        print("Error retrieiving information from OpenAI's API")
                    except KeyboardInterrupt:
                        print("")
                        break
                case "/help" | "/h" | "help" | "h":
                    help()
                case other:
                    sys.exit("Invalid command, terminating program...")
        except KeyboardInterrupt:
            sys.exit("\nProgram has been terminated")


if __name__ == "__main__":
    main()
