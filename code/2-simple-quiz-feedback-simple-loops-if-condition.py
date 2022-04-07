## (2) Simple Quiz - Feedback - Simple Loops and If Condition
## This is a very basic program that tests the user's English vocabulary.
## This lesson introduces while loops and if conditions.
## There is no score. The quiz gives feedback and will not continue until the user gets the answer correct.
## Before this lesson, students already understand:
##   - showing output through print()
##   - string concatenation
##   - taking (keyboard) input from user through input()
##   - variables
## Students will be introduced in:
##   - if conditions
##   - comparison operators (== and !=)
##   - while loops


# Introduction
print("Test your English vocabulary!")
name = input("What is your name? ")
print("\nWelcome " + name + "! Here's your first question:")


# Question 1
print("\nWhich word means \"smart\"?")
print("(a) arduous \n(b) intelligent \n(c) charming")
answer = input("Enter your guess: ")

while(answer != "b"):
    answer = input("Not quite... Try again:")

if(answer == "b"):
    print("Correct!")

# Question 2
print("\nWhich word means \"fearless\"?")
print("(a) airy \n(b) very tired \n(c) brave")
answer = input("Enter your guess: ")

while(answer != "c"):
    answer = input("Not quite... Try again: ")

if(answer == "c"):
    print("Correct!")

# Question 3
print("\nWhich word means \"afterward\"?")
print("(a) maybe \n(b) later \n(c) also")
answer = input("Enter your guess: ")

while(answer != "b"):
    answer = input("Not quite... Try again: ")

if(answer == "b"):
    print("Correct!")

# Question 4
print("\nWhich word means \"eliminate\"?")
print("(a) remove \n(b) chuckle \n(c) slap")
answer = input("Enter your guess: ")

while(answer != "a"):
    answer = input("Not quite... Try again: ")

if(answer == "a"):
    print("Correct!")

# Question 5
print("\nWhich word means \"lasting\"?")
print("(a) sick \n(b) unknown \n(c) permanent")
answer = input("Enter your guess: ")

while(answer != "c"):
    answer = input("Not quite... Try again: ")

if(answer == "c"):
    print("Correct!")

# Question 6
print("\nWhich word means \"clone\"?")
print("(a) gibberish \n(b) duplicate \n(c) finish")
answer = input("Enter your guess: ")

while(answer != "b"):
    answer = input("Not quite... Try again: ")

if(answer == "b"):
    print("Correct!")

# Question 7
print("\nWhich word means \"doubtful\"?")
print("(a) outer \n(b) frightened \n(c) questionable")
answer = input("Enter your guess: ")

while(answer != "c"):
    answer = input("Not quite... Try again: ")

if(answer == "c"):
    print("Correct!")

# Question 8
print("\nWhich word means \"stitch\"?")
print("(a) pulsate \n(b) sew \n(c) discontinue")
answer = input("Enter your guess: ")

while(answer != "b"):
    answer = input("Not quite... Try again: ")

if(answer == "b"):
    print("Correct!")

# Question 9
print("\nWhich word means \"banquet\"?")
print("(a) feast \n(b) flower \n(c) stamp")
answer = input("Enter your guess: ")

while(answer != "a"):
    answer = input("Not quite... Try again: ")

if(answer == "a"):
    print("Correct!")

# Question 10
print("\nWhich word means \"compliment\"?")
print("(a) opposition \n(b) manufacture \n(c) praise")
answer = input("Enter your guess: ")

while(answer != "c"):
    answer = input("Not quite... Try again: ")

if(answer == "c"):
    print("Correct!")

print("*********************************************")
print("You've finished the quiz. Congratulations!")

# Prevents the app from closing prematurely  
exit = input("Press ENTER to exit...")
print(exit)

