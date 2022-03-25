## This is a very basic program that tests the user's English vocabulary.
## It only contains print() and input() functions and doesn't use loops or conditions.
## It will show the score at the end of the quiz.
## Students will be introduced in:
##   - showing output through print()
##   - taking (keyboard) input from user through input()
##   - variables
##   - escape characters using \
##   - addition assignment operator


# Introduction
print("Test your English vocabulary!")
name = input("What is your name? ")
print("\nWelcome " + name + "! Here's your first question:")
score = 0


# Question 1
print("\nWhich word means \"smart\"?")
print("(a) arduous \n(b) intelligent \n(c) charming")
answer = input("Enter your guess: ")

if(answer == "b"):
    score += 1

# Question 2
print("\nWhich word means \"fearless\"?")
print("(a) airy \n(b) very tired \n(c) brave")
answer = input("Enter your guess: ")

if(answer == "c"):
    score += 1

# Question 3
print("\nWhich word means \"afterward\"?")
print("(a) maybe \n(b) later \n(c) also")
answer = input("Enter your guess: ")

if(answer == "b"):
    score += 1

# Question 4
print("\nWhich word means \"eliminate\"?")
print("(a) remove \n(b) chuckle \n(c) slap")
answer = input("Enter your guess: ")

if(answer == "a"):
    score += 1


# Question 5
print("\nWhich word means \"lasting\"?")
print("(a) sick \n(b) unknown \n(c) permanent")
answer = input("Enter your guess: ")

if(answer == "c"):
    score += 1

# Question 6
print("\nWhich word means \"clone\"?")
print("(a) gibberish \n(b) duplicate \n(c) finish")
answer = input("Enter your guess: ")

if(answer == "b"):
    score += 1

# Question 7
print("\nWhich word means \"doubtful\"?")
print("(a) outer \n(b) frightened \n(c) questionable")
answer = input("Enter your guess: ")

if(answer == "c"):
    score += 1

# Question 8
print("\nWhich word means \"stitch\"?")
print("(a) pulsate \n(b) sew \n(c) discontinue")
answer = input("Enter your guess: ")

if(answer == "b"):
    score += 1

# Question 9
print("\nWhich word means \"banquet\"?")
print("(a) feast \n(b) flower \n(c) stamp")
answer = input("Enter your guess: ")

if(answer == "a"):
    score += 1

# Question 10
print("\nWhich word means \"compliment\"?")
print("(a) opposition \n(b) manufacture \n(c) praise")
answer = input("Enter your guess: ")

if(answer == "c"):
    score += 1

print("**********************************************")
print("You've finished the quiz. You got " + str(score) + " out of 10!")

# Prevents the app from closing prematurely  
exit = input("Press ENTER to exit...")
print(exit)
