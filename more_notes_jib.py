# conditinal lotes for larose

grade = 100


if grade >= 90:
    print("You have an A, please get a life nerd")
elif grade >= 70:
    print("You are passing")
else:
    print("You are not passing")
    print("Take it easy pal")

username = input("What is your username: ")

if bool(username):
    print("You didn't type it in")
elif username == "LaRose":
    print('You are the teacher')
else:
    print("You are a student")

raining = False

if raining:
    print("Bring an unmbrella and a jacket")
else:
    print("Wear something else")