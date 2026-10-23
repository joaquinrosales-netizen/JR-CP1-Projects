import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        guess = int(input("Guess a number between 1 and 20: "))
        guesses = guesses + 1

#This line was missing a colon and I added it, SyntaxError, if statements need colons after it, and it wasn't working but I saved the day
        if guess == secret_number:
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---")
#needed an f string so it could properly run, TypeError, this bug stopped the game from running because guesses is supposed to be an integer, and it needed to be properly formatted
print(f"Your guesses per round: {guesses}")

total = 0
for score in scores:
    total = 0
    total = total + score

average = total / rounds
print("Your average guesses per round was " + str(average))

best_round = scores[0]
for i in range(1, rounds - 1):
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")
# program is fully running