# JR escape room project CS 1\

import random
import time

escape_code = random.randint(1, 9999)
freedom_code = random.randint(1, 1000000)

print("Welcome to BlobGPT")
print("You have commited too many crimes against China")
print("Therefore, you have been placed in prison, and in order to escape, you must well, escape")
print("You are to guess a number between one and 9999")
print("Good luck")

while True:
    try:
        guess = int(input("Type what you think the code is right here: "))

        if guess > escape_code:
            print("You got the number a bit too big, capital L Loser, you need to do math.")
        elif guess < escape_code:
            print("You got the number a little bit too small lil bro, your a noob, try again.")
        elif guess == escape_code:
            print("You got the code correct. You are free to leave.🤠")
            time.sleep(1)
            print("SIIIIKEEE")
            time.sleep(1)
            print("YOU HAVE TO DO ONE MORE ESCAPE ROOM, SERIOUSLY HOW DID YOU FALL FOR THAT?")
            print("This time, it will be one number in between one, and, one million!")
            print("Have fun with this one")
            time.sleep(2)
            print("😁👍")
            time.sleep(2)
            guess_freedom = int(input("Type what you think the new code is right here: "))
            if guess_freedom == freedom_code:
                print("Welp, ya made it, guess we have to say goodbye now...this was fun you know")
                time.sleep(3)
                print("SIIIIIKEEE")
                print("I only have one more question before you go!")
                time.sleep(1)
                champions_league_winner = input("IS PSG GONNA WIN THE CHAMPIONS LEAGUE?!?!?!").strip().title()
                if champions_league_winner == "Yes":
                    print("YESSSS LETS GOOOOO WE HAVE THE BEST ROSTER OF THE SEASON BABY!!!!!") 
                if champions_league_winner == "No":
                    print("NOOOO A PSG HATER PARIS WILL WIN THE LEAGUE!!!")
                break
            elif guess_freedom > freedom_code:
                print("You got the number a bit too big, do the task bro think about it")
            elif guess_freedom < freedom_code:
                print("The number ya guessed is too small, try again, loser😆😆😆😆")
    except ValueError:
        print("Read the instructions you chud, IT VERBALLY SAYS YOU NEED TO PUT IN A NUMBER, DO I HAVE TO REPEAT MYSELF, N-U-M-B-E-R")

