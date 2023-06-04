import openai
import os
import pytest

from dotenv import load_dotenv
from functions import chat_helper

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def test_chat(monkeypatch):
     monkeypatch.setattr('builtins.input', lambda _: "Hi how are you?")
     previous_questions_and_answers = []
     assert chat_helper(previous_questions_and_answers) == 0
     
     monkeypatch.setattr('builtins.input', lambda _: "How's your day?")
     previous_questions_and_answers = []
     assert chat_helper(previous_questions_and_answers) == 0
     
     monkeypatch.setattr('builtins.input', lambda _: "What is 10+10?")
     previous_questions_and_answers = []
     assert chat_helper(previous_questions_and_answers) == 0
     
     