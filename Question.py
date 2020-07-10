class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def check_anser(self, user_answer):
        return user_answer == self.answer
