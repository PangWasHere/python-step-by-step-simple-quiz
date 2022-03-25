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


# Introduction
print("Test your English vocabulary!")
name = input("What is your name? ")
print("\nWelcome " + name + "! Here's your first question:")

# Creating the questions using a dictionary
questions = [
        {
            'word': 'smart',
            'choices': "(a) arduous \n(b) intelligent \n(c) charming",
            'answer': 'b'
        },
        {
            'word': 'fearless',
            'choices': "(a) airy \n(b) very tired \n(c) brave",
            'answer': 'c'
        },
        {
            'word': 'afterward',
            'choices': "(a) maybe \n(b) later \n(c) also",
            'answer': 'b'
        },
        {
            'word': 'eliminate',
            'choices': "(a) remove \n(b) chuckle \n(c) slap",
            'answer': 'a'
        },
        {
            'word': 'lasting',
            'choices': "(a) sick \n(b) unknown \n(c) permanent",
            'answer': 'c'
        },
        {
            'word': 'clone',
            'choices': "(a) gibberish \n(b) duplicate \n(c) finish",
            'answer': 'b'
        },
        {
            'word': 'doubtful',
            'choices': "(a) outer \n(b) frightened \n(c) questionable",
            'answer': 'c'
        },
        {
            'word': 'stitch',
            'choices': "(a) pulsate \n(b) sew \n(c) discontinue",
            'answer': 'b'
        },
        {
            'word': 'banquet',
            'choices': "(a) feast \n(b) flower \n(c) stamp",
            'answer': 'a'
        },
        {
            'word': 'compliment',
            'choices': "(a) opposition \n(b) manufacture \n(c) praise",
            'answer': 'c'
        }
    ]

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

