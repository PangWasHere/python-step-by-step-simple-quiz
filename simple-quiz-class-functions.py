## This is a very basic program that tests the user's English vocabulary.
## It only contains print() and input() functions. It introduces if conditions, while and for loops, and lists.
## The quiz will not continue until the user gets the answer correct.
## Students will be introduced in:
##   - showing output through print()
##   - taking (keyboard) input from user through input()
##   - variables
##   - if conditions
##   - while and for loops
##   - escape characters
##   - lists
##   - classes

from Question import Question
from listQuestions import questions as questions_list

# Initialize values
questions = []
for question in questions_list:
    questions.append(Question.convertListToClass())



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

