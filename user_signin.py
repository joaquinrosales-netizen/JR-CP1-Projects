#joaquin rosales user sign in assignment
user = input("Please type in a new username: ")

password = input("Please type in a new password: ")
print("Ok you will now type your username and password again.")

username = input("Please type in the correct username: ")

passkey = input("Please type in the correct password: ")

if passkey == password and username == user:
    print("Login succesful")
else:
    print("Login unsuccessful")