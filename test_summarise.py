import openai
import os
import pytest

from dotenv import load_dotenv
from functions import summarise

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def test_summarise(monkeypatch):
     monkeypatch.setattr('builtins.input', lambda _: "Learn to program with our beginner-friendly tutorials and examples. Read tutorials, try examples, write code and learn to program.")
     assert summarise() == 0

def test_short(monkeypatch):
     monkeypatch.setattr('builtins.input', lambda _: "Hi")
     assert summarise() == 1