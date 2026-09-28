# JR CS1 letter grade assignment

class_amount = int(input("How many classes do you have?(only put in 2-8 classes): "))

if class_amount == 2:
    class_one = input("What is your number grade in your first class?: ")
    class_two = input("What is your number grade in your second class?: ")
elif class_amount == 3:
    class_one = input("What is your number grade in your first class?: ")
    class_two = input("What is your number grade in your second class?: ")
    class_three = input("What is your number grade in your third class?: ")
elif class_amount == 4:
    class_one = input("What is your number grade in your first class?: ")
    class_two = input("What is your number grade in your second class?: ")
    class_three = input("What is your number grade in your third class?: ")
    class_four = input("What is your number grade in your fourth class?: ")
elif class_amount == 5:
    class_one = input("What is your number grade in your first class?: ")
    class_two = input("What is your number grade in your second class?: ")
    class_three = input("What is your number grade in your third class?: ")
    class_four = input("What is your number grade in your fourth class?: ")
    clasS_five = input("What is your number grade in your fifth class?: ")
else:
    print("Please put in 2-8 classes")