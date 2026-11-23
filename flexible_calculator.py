#JR Flexible Calculator
import math

def question(equation, *question_type):
    while True:
        question_choice = input(equation).strip().lower()
        if question_choice in question_type:
            return(question_choice)
        print("The input wasn't correct. Please spell correctly")
        break

def actual_number():
    print("Enter number (type 'done' when finished)")
    numbers = []
    while True:
        user_message = input("Type the number you would like to calculate: \ndone \naverage \nproduct \nsum \nmin \nmax")
        if user_message == "done":
            break
        
        try:
            numbers.append(float(user_message))
        except ValueError:
            print("Invalid")
        return numbers
    
def calculator(operation, *numbers):
    if operation == "average":
        return sum(numbers) / len(numbers)
    elif operation == "product":
        return math.prod(numbers)