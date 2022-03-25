## (6.2) Simple Quiz - Scored - Functions
## This is a very basic program that tests the user's English vocabulary.
## This lesson introduces functions.
## The quiz is scored and will not give any feedback.
## Please refer to 6-1-simple-quiz-feedback-functions for the feedback version.
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
score = 0
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
        
    if(question.isCorrect(answer)):
        score += 1

print("*******************************************")         
print("You've finished the quiz. You got " + str(score) + " out of 10!")

# Prevents the app from closing prematurely  
exit = input("Press ENTER to exit...")
print(exit)

