#JR while loops notes

import random
import time

goose = random.randint(1,20)
duck = 1

while goose > duck:
    print("Duck. . . ")
    time.sleep(0.25)
    duck += 1

print("GOOSE!")


count = 1

while count < 30:
    print(count)
    time.sleep(.1)
    count += 1

number = random.randint(1,101)


while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < 0 or guess > 100:
                print("You should read the instructions")
        continue
        break
        except:
        print("That isn't a number!")
        if guess == number:
            print("You guessed right!")
        break
        elif guess < number:
        print("That number is too low!")
        elif guess > number:
        print("That number is too high!")
else:
    print("How the heck did you get here brodie")