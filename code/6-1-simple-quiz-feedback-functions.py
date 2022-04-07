## (6.1) Simple Quiz - Feedback - Functions
## This is a very basic program that tests the user's English vocabulary.
## This lesson introduces functions.
## The quiz will not continue until the user gets the answer correct.
## Please refer to 6-2-simple-quiz-scored-functions for the scored version.
## Before this lesson, students already understand:
##   - showing output through print()
##   - string concatenation
##   - taking (keyboard) input from user through input()
##   - variables
##   - if conditions
##   - comparison operators (== and !=)
##   - loops
##   - lists
##   - import
##   - classes
## Students will be introduced in:
##   - functions 

from Question import Question
from questionslist import questions as questions_list

# Initialize values
questions = []
for question in questions_list:
    questions.append(Question.convertListToClass(question))

# Introduction
print("Test your English vocabulary!")
name = input("What is your name? ")
print("\nWelcome " + name + "! Here's your first question:")

for question in questions:
    print("\nWhich word means \"" + question.word + "\"?")
    print(question.choices)
    answer = input("Enter your guess: ")

    while(not question.isCorrect(answer)):
        answer = input("Not quite.. Try again: ")
        
    if(question.isCorrect(answer)):
        print("Correct!\n")

print("*******************************************")         
print("You've finished the quiz. Congratulations!")

# Prevents the app from closing prematurely  
exit = input("Press ENTER to exit...")
print(exit)

