import openai

class Prompt:
    # Constructor functions
    def __init__(self, text):
        self._text = text

    def __str__(self):
        return f"Prompt: {self._text}"
    
    # Using GPT 3.5 to chat with the user with AI-generated responses
    def get_response(self, previous_questions_and_answers):

        # build the messages
        messages = [
            { "role": "system", "content": "You are a friend" },
        ]
        # add the previous questions and answers
        for question, answer in previous_questions_and_answers[-5:]:
            messages.append({ "role": "user", "content": question })
            messages.append({ "role": "assistant", "content": answer })
        # add the new question
        messages.append({ "role": "user", "content": self._text })

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.8
        )
        return completion.choices[0].message.content




