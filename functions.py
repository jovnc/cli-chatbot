from gpt import Prompt
from deep_translator import GoogleTranslator, exceptions


def translate():
    
    out = input("Output Language: ")
    if out.lower() == "chinese":
        out = "chinese (traditional)"
    text = input("Text: ")
    try:
        response = GoogleTranslator(source='auto', target=out.lower()).translate(text)
        print(response)
        return 0
    except exceptions.LanguageNotSupportedException:
        print("Language not supported, please try a different language")
        return 1

def chat():
    try:
        previous_questions_and_answers = []
        while True:
            new_question = input("Input: ")
            prompt = Prompt(new_question)
            response = prompt.get_response(previous_questions_and_answers)
            previous_questions_and_answers.append((new_question, response))
            print(f"Output: {response}")
    except KeyboardInterrupt:
        print("")
        return 1

def help():
    print("""
Welcome to CLI Bot!

Instructions Menu:
/help or /h - show the instructions menu
/translate or /t - translation page
/chat or /c - artificial intelligence powered chatbot
ctrl + c - return to the commands menu
ctrl + z - terminate the program
    """
    )
    
    return 0
    