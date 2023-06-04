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
    while True:
        help("main")
        try:
            i = input("What would you like to do? ")
            match i.lower():
                case "/translate" | "/t" | "translate" | "t":
                    help("translate")
                    while True:
                        try:
                            translate()
                        except KeyboardInterrupt:
                            print("")
                            break
                case "/chat" | "/c" | "chat" | "c":
                    help("chat")
                    try:
                        chat()
                    except openai.error.APIError:
                        print("Error retrieiving information from OpenAI's API")
                    except KeyboardInterrupt:
                        print("")
                        break
                case "/help" | "/h" | "help" | "h":
                    help("main")
                case "/summarise" | "/s" | "s" | "summarise":
                    help("summarise")
                    while True:
                        try:
                            summarise()
                        except KeyboardInterrupt:
                            print("")
                            break
                case other:
                    sys.exit("Invalid command, terminating program...")
        except KeyboardInterrupt:
            print("")
            pass


if __name__ == "__main__":
    main()
