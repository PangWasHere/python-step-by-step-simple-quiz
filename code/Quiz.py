import random

class Quiz:

    def __init__(self, arithmetic_operation, count = 5):
        self.arithmetic_operation = arithmetic_operation
        self.count = count
        self.score = 0

    def validateAnswer(self, user_input):
        valid = True

        # Only accept numbers as a valid answer
        if not user_input.isdigit():
            valid = False
            user_input = input("Seems like you didn't input a number. Try again: ")
            self.validateAnswer(user_input)

        return valid

    def startQuiz(self):
        if(self.arithmetic_operation == "a"):
            self.lauchAdditionQuiz()
        elif(self.arithmetic_operation == "b"):
            self.launchSubtractionQuiz()
        elif(self.arithmetic_operation == "c"):
            self.launchMultiplicationQuiz()
        elif(self.arithmetic_operation == "d"):
            self.launchDivisionQuiz()

    def lauchAdditionQuiz(self):
        for _ in range(self.count):
            first_number = random.randint(1,100)
            second_number = random.randint(1,100)
            answer = first_number + second_number
            user_answer = input(str(first_number) + " + " + str(second_number) + " = ")

            self.validateAnswer(user_answer)

            self.showAnswer(user_answer, answer)

    def launchSubtractionQuiz(self):
        for _ in range(self.count):
            first_number = random.randint(20,100)
            second_number = random.randint(20,100)

            while(first_number < second_number):
                first_number = random.randint(20,100)
                second_number = random.randint(20,100)

            answer = first_number - second_number
            user_answer = input(str(first_number) + " - " + str(second_number) + " = ")

            self.validateAnswer(user_answer)

            self.showAnswer(user_answer, answer)

    def launchMultiplicationQuiz(self):
        for _ in range(self.count):
            first_number = random.randint(2,20)
            second_number = random.randint(2,20)
            answer = first_number * second_number
            user_answer = input(str(first_number) + " x " + str(second_number) + " = ")

            self.validateAnswer(user_answer)

            self.showAnswer(user_answer, answer)

    def launchDivisionQuiz(self):
        for _ in range(self.count):
            first_number = random.randint(20,500)
            second_number = random.randint(1,100)

            while(first_number % second_number != 0 or first_number < second_number):
                first_number = random.randint(20,500)
                second_number = random.randint(1,100)

            answer = int(first_number / second_number)
            user_answer = input(str(first_number) + " / " + str(second_number) + " = ")

            self.validateAnswer(user_answer)

            self.showAnswer(user_answer, answer)

    def showAnswer(self, user_answer, answer):
        if(user_answer == str(answer)):
            self.score += 1
        else:
            print("The correct answer is: " + str(answer))