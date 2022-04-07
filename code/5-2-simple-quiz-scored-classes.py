## (5.2) Simple Quiz - Scored - Classes
## This is a very basic program that tests the user's English vocabulary.
## This lesson introduces classes.
## The quiz is scored and will not give any feedback.
## Please refer to 5-1-simple-quiz-feedback-classes for the feedback version.
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
## Students will be introduced in:
##   - classes

class Question:
   def __init__(self, word, choices, answer):
       self.word = word
       self.choices = choices
       self.answer = answer

# Initialize values
score = 0
questions = [
        Question("smart", "(a) arduous \n(b) intelligent \n(c) charming", "b"),
        Question("fearless", "(a) airy \n(b) very tired \n(c) brave", "c"),
        Question("afterward", "(a) maybe \n(b) later \n(c) also", "b"),
        Question("eliminate", "(a) remove \n(b) chuckle \n(c) slap", "a"),
        Question("lasting", "(a) sick \n(b) unknown \n(c) permanent", "c"),
        Question("clone", "(a) gibberish \n(b) duplicate \n(c) finish", "b"),
        Question("doubtful", "(a) outer \n(b) frightened \n(c) questionable", "c"),
        Question("stitch", "(a) pulsate \n(b) sew \n(c) discontinue", "b"),
        Question("banquet", "(a) feast \n(b) flower \n(c) stamp", "a"),
        Question("compliment", "(a) opposition \n(b) manufacture \n(c) praise", "c"),
    ]

# Introduction
print("Test your English vocabulary!")
name = input("What is your name? ")
print("\nWelcome " + name + "! Here's your first question:")


for question in questions:
    print("\nWhich word means \"" + question.word + "\"?")
    print(question.choices)
    answer = input("Enter your guess: ")
        
    if(answer == question.answer):
        score += 1

print("*******************************************")         
print("You've finished the quiz. You got " + str(score) + " out of 10!")

# Prevents the app from closing prematurely  
exit = input("Press ENTER to exit...")
print(exit)

