## (Extras) Simple Quiz - Randomised
## This version of the simple quiz shuffles the questions everytime the code is run.
## This code introduces a commonly used Python library called random.
## The quiz gives a score at the end of the quiz and gives immediate feedback.
## Please refer to extras-simple-quiz-scored-with-feedback.

## Further learning:
## random is one of the built-in libraries readily available to be added in your Python code.
## To learn more about Python Standard Library, please refer to https://docs.python.org/3/library/


import random

from Question import Question
from questionslist import questions as questions_list

# Initialize values
score = 0
questions = []
for question in questions_list:
    questions.append(Question.convertListToClass(question))

random.shuffle(questions)   # Shuffle questions

# Introduction
print("Test your English vocabulary!")
name = input("What is your name? ")
print("\nWelcome " + name + "! Here's your first question:")

for question in questions:
    print("\nWhich word means \"" + question.word + "\"?")
    print(question.choices)
    answer = input("Enter your guess: ")
        
    if(question.isCorrect(answer)):
        print("Correct!\n")
        score += 1
    else:
        print("Oops.. The correct answer is " + question.answer + ".\n")
    
    input("Press ENTER to continue...")     # Forced pause

print("*******************************************")         
print("You've finished the quiz. Congratulations!")

# Prevents the app from closing prematurely  
exit = input("Press ENTER to exit...")
print(exit)

