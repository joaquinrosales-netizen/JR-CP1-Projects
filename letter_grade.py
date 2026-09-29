# JR CS1 letter grade assignment

class_amount = int(input("How many classes do you have?(only put in 2-8 classes): "))

if class_amount == 2:
    class_one = float(input("What is your number grade in your first class?: "))
    class_two = float(input("What is your number grade in your second class?: "))
elif class_amount == 3:
    class_one = float(input("What is your number grade in your first class?: "))
    class_two = float(input("What is your number grade in your second class?: "))
    class_three = float(input("What is your number grade in your third class?: "))
elif class_amount == 4:
    class_one = float(input("What is your number grade in your first class?: "))
    class_two = float(input("What is your number grade in your second class?: "))
    class_three = float(input("What is your number grade in your third class?: "))
    class_four = float(input("What is your number grade in your fourth class?: "))
elif class_amount == 5:
    class_one = float(input("What is your number grade in your first class?: "))
    class_two = float(input("What is your number grade in your second class?: "))
    class_three = float(input("What is your number grade in your third class?: "))
    class_four = float(input("What is your number grade in your fourth class?: "))
    class_five = float(input("What is your number grade in your fifth class?: "))
elif class_amount == 6:
    class_one = float(input("What is your number grade in your first class?: "))
    class_two = float(input("What is your number grade in your second class?: "))
    class_three = float(input("What is your number grade in your third class?: "))
    class_four = float(input("What is your number grade in your fourth class?: "))
    class_five = float(input("What is your number grade in your fifth class?: "))
    class_six = float(input("What is your number grade in your sixth class?: "))
elif class_amount == 7:
    class_one = float(input("What is your number grade in your first class?: "))
    class_two = float(input("What is your number grade in your second class?: "))
    class_three = float(input("What is your number grade in your third class?: "))
    class_four = float(input("What is your number grade in your fourth class?: "))
    class_five = float(input("What is your number grade in your fifth class?: "))
    class_six = float(input("What is your number grade in your sixth class?: "))
    class_seven = float(input("What is your number grade in your seventh class?: "))
elif class_amount == 8:
    class_one = float(input("What is your number grade in your first class?: "))
    class_two = float(input("What is your number grade in your second class?: "))
    class_three = float(input("What is your number grade in your third class?: "))
    class_four = float(input("What is your number grade in your fourth class?: "))
    class_five = float(input("What is your number grade in your fifth class?: "))
    class_six = float(input("What is your number grade in your sixth class?: "))
    class_seven = float(input("What is your number grade in your seventh class?: "))
    class_eight = float(input("What is your grade in your eight class?: "))
else:
    print("Please put in 2-8 classes")

if class_amount == 2:
    number_grade = (class_amount + class_one + class_two) / 2
elif class_amount == 3:
    number_grade = (class_amount + class_one + class_two + class_three) / 3
elif class_amount == 4:
    number_grade = (class_amount + class_one + class_two + class_three + class_four) / 4
elif class_amount == 5:
    number_grade = (class_amount + class_one + class_two + class_three + class_four + class_five) / 5
elif class_amount == 6:
    number_grade = (class_amount + class_one + class_two + class_three + class_four + class_five + class_six) / 6
elif class_amount == 7:
    number_grade = (class_amount + class_one + class_two + class_three + class_four + class_five + class_six + class_seven) / 7
elif class_amount == 8:
    number_grade = (class_amount + class_one + class_two + class_three + class_four + class_five + class_six + class_seven + class_eight) / 8

number_grade_two = round(number_grade)
print(number_grade_two)

if number_grade_two >= 93:
    print("You have an A, you friggin nerd. Get a life man.")
if number_grade_two >= 90:
    print("You have an A- ,your trying too hard, take a chill pill")
if number_grade_two >= 87:
    print("You have a B+ ,good job brother, give yourself a pat on the back :)")
if number_grade_two >= 83:
    print("You got a B, take it easy pal")
if number_grade_two >= 80:
    print("You got a B-, take it easy brother")
if number_grade_two >= 77:
    print("You got a C+, time to get to work!")
if number_grade_two >= 73:
    print("You got a C, you gotta improve on some things")
if number_grade_two >= 70:
    print("You got a C-,keep going man, you can do this, you can get an A")
if number_grade_two >= 67:
    print("You got a D+, you probably ain't even trying at this point.")
if number_grade_two >= 60:
    print("You got a D,noob, lol .")
if number_grade_two >= 0:
    print("You have an F,🥀💔")