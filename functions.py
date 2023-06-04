from gpt import Prompt
from deep_translator import GoogleTranslator, exceptions


def translate():
    """This function prompts the user for two inputs: language and text, and will use deep_translator to translate the given text into the desired language specified by the user. If the language is not found, it will throw an error and print it out
    
    Return: 0 if successful and 1/2 if not successful
    """
    
    out = input("Output Language: ")
    if out.lower() == "chinese":
        out = "chinese (traditional)"
    text = input("Text: ")
    try:
        if text.isnumeric():
            raise ValueError
        response = GoogleTranslator(source='auto', target=out.lower()).translate(text)
        print(response)
        return 0
    except exceptions.LanguageNotSupportedException:
        print("Language not supported, please try a different language")
        return 1
    except ValueError:
        print("Text needs to contain alphabets to be translated")
        return 2

def chat():
    """This function uses the chat_helper() function to continuously prompt the user for input until KeyboardInterrupt is executed and the program will terminate and return to the home page.
    
    Return: 0 if successful and 1 if KeyboardInterrupt occurs
    """
    try:
        previous_questions_and_answers = []
        while True:
            chat_helper(previous_questions_and_answers)
    except KeyboardInterrupt:
        print("")
        return 1
    
def chat_helper(previous_questions_and_answers):
    """This is a helper function to the chat() function which prompts the user for input and generates an AI output using GPT 3.5 to be printed.
    
    Return: 0 if successful
    """
    new_question = input("Input: ")
    prompt = Prompt(new_question)
    response = prompt.get_response(previous_questions_and_answers)
    previous_questions_and_answers.append((new_question, response))
    print(f"Output: {response}")
    return 0

def summarise():
    """This function prompts the user for a text input and prints the summarised version of the text, returning an error if the text is too short to be summarised.

    Return: 0 if successful and 1 if not successful
    """
    
    text = input("Input: ")
    prompt = Prompt(text)
    summary = prompt.summarise()
    if len(summary) >= len(text):
        print("Text is too short to be summarised, please retry with longer text")
        return 1
    print(f"Output: {summary}")
    return 0


def help(section):
    """This function prints the relevant information on the command line to guide users on how to use the CLI bot according to which section that the user is accessing in the bot.

    Return: 0 if successful
    """
    
    match section:
        case "main":
            print("""
Welcome to CLI Bot!

Instructions Menu:
/help or /h - show the instructions menu
/translate or /t - translation page
/chat or /c - general purpose chatbot
/summarise or /s - summarise text
ctrl + c - return to the commands menu
ctrl + z - terminate the program
    """
    )
        case "chat":
            print("""
Welcome to CLI Bot Chatbot! 
          
Instructions for use:
1. Ask the bot anything and wait for response!
2. If your output is too long, it might take a longer time to generate the output or might even encounter errors in fetching the API response -> fix: try to ask shorter questions instead

To terminate the programme, use ctrl + z
To return to the commands menu, use ctrl + c 
""")
        case "translate":
            print("""
Welcome to CLI Bot Translation! 
          
Instructions for use:
1. Write the desired output language in the terminal as prompted in the command line
2. Write the text that you wish to translate (the bot will automatically detect the language that you wrote in)
3. Wait for the output to print on the command line

To terminate the programme, use ctrl + z
To return to the commands menu, use ctrl + c 
""")
        case "summarise":
            print("""
Welcome to CLI Bot Summarise! 
          
Instructions for use:
1. Write the text that you wish to summarise (make sure that it is of sufficient length to be summarised)
2. Wait for the output to print on the command line

To terminate the programme, use ctrl + z
To return to the commands menu, use ctrl + c 
""")
    
    return 0
    
