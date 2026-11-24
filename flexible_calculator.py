#JR flexible calculator
import math

def question(equation, *question_type):
    while True:
        question_choice = input(equation).strip().lower()

        if question_choice in question_type:
            return question_choice

        print("The input wasn't correct. Please spell it correctly.")

#where the user inputs the numbers calculated
def actual_number():
    print("Enter numbers (type 'done' when finished)")
    numbers = []

    while True:
        user_message = input("Enter a number: ").strip().lower()

        if user_message == "done":
            break

        try:
            numbers.append(float(user_message))
        except ValueError:
            print("Invalid number")

    return numbers

#where the math happens
def calculator(operation, *numbers):
    if operation == "average":
        return sum(numbers) / len(numbers)

    elif operation == "product":
        return math.prod(numbers)

    elif operation == "sum":
        return sum(numbers)

    elif operation == "min":
        return min(numbers)

    elif operation == "max":
        return max(numbers)


# Runs the actual program
numbers = actual_number()

if len(numbers) == 0:
    print("You didn't enter any numbers.")

else:
    operation = question(
        "Choose: average, product, sum, min, max: ",
        "average", "product", "sum", "min", "max"
    )

    result = calculator(operation, *numbers)

    print("The result is:", result)
