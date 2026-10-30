# JR password strength checker code
points = []
specials = ["~","`","!","@","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}","|","'",'"',":",";","<",">",",",".","?","/"]

while True:

    print("You are going to enter a password and the program is going to check how strong it is.")
    password = input("Please choose a password: ")

    def length(password):
        return len(password) >= 8
    if not length(password):
        print("Your password is not long enough")
    else:
        points.append( 1 )

    if not any(char.isupper() for char in password):
        print("Your password does not contain a capital")
    else:
        points.append( 1 )
    if not any(char.islower() for char in password):
        print("Your password does not have a lower case letter.")
    else:
        points.append( 1 )
    if not any(char.isnumeric() for char in password):
        print("Your password does not have any numbers")
    else:
        points.append( 1 )
    if not any(char in specials for char in password):
        print("Your password does not have any special characters")
    else:
        points.append( 1 )
    points_grading = sum(points)
    print("Your score based on password strength is " ,points_grading, ".")
    if points_grading == 5:
        print("This is a very strong password")
    if points_grading == 4:
        print("This is a strong password")
    if points_grading == 3:
        print("This is a moderate password")
    if points_grading == 2:
        print("This is a weak password")
    if points_grading == 1:
        print("This is a very weak password")
    break