# JR password strength checker code

specials = ["~","`","!","@","#","$","%","^","&","*","(",")", "_","-","+","=","{","[","]","}","|",":",";","'",'"',"<",",",">",".","?","/"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
cap = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

while True:

    print("You are going to enter a password and the program is going to check how strong it is.")
    password = input("Please choose a password: ")

    def length(password):
        return len(password) >= 8
    if not length(password):
        print("Your password is not long enough")

    if not any(char.isupper() for char in password):
        print("Your password does not contain a capital")
    
    if not any(char.islower() for char in password):
        print("Your password does not have a lower case letter.")
    
    if password not in numbers:
        print("Your password does not have any numbers")

        break