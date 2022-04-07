## (Extras) Simple Quiz - Scored with Feedback
## Throughout the lessons, you've seen two different ways the quiz is assessed:
##    - Scored
##    - Immediate feedback
## The following code uses both approaches where user is scored if the question is answered correctly in the first guess,
## and the correct answer is shown when the first guess is wrong.

## Critical thinking opportunity:
## This is an opportunity for you to think about UX theory. 
## Notice that in this code, we added a "pause" after the user enter their guess.
## What do you think is the purpose of this "pause"? 
## Remove the code enforcing the pause and run the quiz.
## How is your experience this time around?
## Does the pause enhance or disrupts user experience?
## Do you think user experience is consistent for ALL users?
## Ask your classmates how they felt about the "pause".


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
        print("Correct!\n")
        score += 1
    else:
        print("Oops.. The correct answer is " + question.answer + ".\n")
    
    input("Press ENTER to continue...")     # Forced pause

print("*******************************************")         
print("You've finished the quiz. You got " + str(score) + " out of 10!")

# Prevents the app from closing prematurely  
exit = input("Press ENTER to exit...")
print(exit)

