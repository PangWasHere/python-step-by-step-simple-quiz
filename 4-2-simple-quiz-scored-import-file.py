## (4.2) Simple Quiz - Scored - Import File
## This is a very basic program that tests the user's English vocabulary.
## This lesson introduces importing files and variables withing Python files.
## The quiz is scored and will not give any feedback.
## Please refer to 4-1-simple-quiz-feedback-import-file for the feedback version.
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

# Initialize
score = 0

# Introduction
print("Test your English vocabulary!")
name = input("What is your name? ")
print("\nWelcome " + name + "! Here's your first question:")


for question in questions:
    print("\nWhich word means \"" + question['word'] + "\"?")
    print(question['choices'])
    answer = input("Enter your guess: ")
        
    if(answer == question['answer']):
        score +=1

print("*********************************************")        
print("You've finished the quiz. You got " + str(score) + " out of 10!")

# Prevents the app from closing prematurely  
exit = input("Press ENTER to exit...")
print(exit)

