## (4.1) Simple Quiz - Feedback - Import File
## This is a very basic program that tests the user's English vocabulary.
## This lesson introduces importing files and variables withing Python files.
## The quiz will not continue until the user gets the answer correct.
## Please refer to 4-2-simple-quiz-scored-import-file for the scored version.
## Before this lesson, students already understand:
##   - showing output through print()
##   - string concatenation
##   - taking (keyboard) input from user through input()
##   - variables
##   - if conditions
##   - comparison operators (== and !=)
##   - loops
##   - lists
## Students will be introduced in:
##   - import

from questionslist import questions

# Introduction
print("Test your English vocabulary!")
name = input("What is your name? ")
print("\nWelcome " + name + "! Here's your first question:")


for question in questions:
    print("\nWhich word means \"" + question['word'] + "\"?")
    print(question['choices'])
    answer = input("Enter your guess: ")

    while(answer != question['answer']):
        answer = input("Not quite.. Try again: ")
        
    if(answer == question['answer']):
        print("Correct!")

print("*********************************************")        
print("You've finished the quiz. Congratulations!")

# Prevents the app from closing prematurely  
exit = input("Press ENTER to exit...")
print(exit)

