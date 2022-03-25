class Question:
    def __init__(self, word, choices, answer):
        self.word = word
        self.choices = choices
        self.answer = answer

    def isCorrect(self, guess):
        correct = False
        if(guess == self.answer):
            correct = True

        return correct
    
    def convertListToClass(question):
        return Question(question['word'], question['choices'], question['answer'])