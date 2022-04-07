


from Quiz import Quiz
import os

# Introduction
def showIntroduction():
    print("Choose an arithmetic operation (Input its corresponding letter):")
    print("(a) Addition \n(b) Subtraction \n(c) Multiplication \n(d) Division")
    arithmetic_operation = input("Arithmetic Operation: ")

    # Only accepts "a", "b", "c", "d" as valid input
    while(arithmetic_operation != "a" and arithmetic_operation != "b" and arithmetic_operation != "c" and arithmetic_operation != "d"):
        arithmetic_operation = input("Please input the corresponding letter of the operation: ")

    # Initialize
    quiz = Quiz(arithmetic_operation)

    quiz.startQuiz()

    print("You got " + str(quiz.score) + " correct answers out of " + str(quiz.count) + "!")
    try_again = input("Would you like to try again? Enter y for \"yes\", else press any key to exit...")

    if(try_again == "y" or try_again == "yes"):
        os.system('cls')    # Clears the screen
        showIntroduction()  # Calls the function again (Notice that we're calling the function inside itself? This is called a recursion.)

showIntroduction()