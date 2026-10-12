# JR escape room project CS 1\

import random

escape_code = random.randint(1,9999)

print("Welcome to BlobGPT")
print("You have commited too many crimes against China")
print("Therefore, you have been placed in prison, and in order to escape, you must well, escape")
print("You are to guess a number between one and 9999")
print("Good luck")

while True:
        try:
            guess = int(input("Type what you think the code is right here: "))

        if guess == escape_code:
            print("You got the code correct. You are free to leave.")
        elif guess > escape_code:
            print("You got the number a bit too big, try again.")
        elif guess < escape_code:
            print("You got the number a little bit too small, try again.")
