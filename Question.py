class Question:
    def __init__(self, word, choices, answer):  # Instance method
        self.word = word
        self.choices = choices
        self.answer = answer

    def isCorrect(self, guess):                 # Class Method (Introduced in Lesson 6)
        correct = False
        if(guess == self.answer):
            correct = True

        return correct
    
    @staticmethod
    def convertListToClass(question):           # Static Method (Introduced in Lesson 6)
        return Question(question['word'], question['choices'], question['answer'])