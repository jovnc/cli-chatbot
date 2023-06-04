from functions import help

def test_help_main(capfd):
    help("main")
    out, err = capfd.readouterr()
    assert out == """
Welcome to CLI Bot!

Instructions Menu:
/help or /h - show the instructions menu
/translate or /t - translation page
/chat or /c - general purpose chatbot
/summarise or /s - summarise text
ctrl + c - return to the commands menu
ctrl + z - terminate the program
    \n"""
    assert help("main") == 0
    
def test_help_translate(capfd):
    help("translate")
    out, err = capfd.readouterr()
    assert out == """
Welcome to CLI Bot Translation! 
          
Instructions for use:
1. Write the desired output language in the terminal as prompted in the command line
2. Write the text that you wish to translate (the bot will automatically detect the language that you wrote in)
3. Wait for the output to print on the command line

To terminate the programme, use ctrl + z
To return to the commands menu, use ctrl + c 
\n"""
    assert help("translate") == 0
    
def test_help_chat(capfd):
    help("chat")
    out, err = capfd.readouterr()
    assert out == """
Welcome to CLI Bot Chatbot! 
          
Instructions for use:
1. Ask the bot anything and wait for response!
2. If your output is too long, it might take a longer time to generate the output or might even encounter errors in fetching the API response -> fix: try to ask shorter questions instead

To terminate the programme, use ctrl + z
To return to the commands menu, use ctrl + c 
\n"""
    assert help("chat") == 0
    
def test_help_summarise(capfd):
    help("summarise")
    out, err = capfd.readouterr()
    assert out == """
Welcome to CLI Bot Summarise! 
          
Instructions for use:
1. Write the text that you wish to summarise (make sure that it is of sufficient length to be summarised)
2. Wait for the output to print on the command line

To terminate the programme, use ctrl + z
To return to the commands menu, use ctrl + c 
\n"""
    assert help("summarise") == 0