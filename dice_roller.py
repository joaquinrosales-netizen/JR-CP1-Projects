import random

print("Welcome to BlobGPT")
print("I want to play a game with you buddy boy")
gameaccept = input("Do you accept the game? (yes/no question only): ").capitalize().strip()
if gameaccept == "Yes":
    print("Ok let's begin")
if gameaccept == "No":
    print("(information sold to China)Welp, sucks to suck")
print('Ok, let\'s play now!')
dice = input("What dice do you want to roll? (D4, D6, D8, D10, D12, D14, D16, D18, D20): ").strip().upper()
D4 = random.randint(1,4)
if dice == "D4":
        print(f"You rolled a {D4}!")
D6 = random.randint(1,6)
if dice == "D6":
    print(f"You rolled a {D6}!")
D8 = random.randint(1,8)
if dice == "D8":
    print(f"You rolled a {D8}!")
D10 = random.randint(1,10)
if dice == "D10":
    print(f"You rolled a {D10}!")
D12 = random.randint(1,12)
if dice == "D12":
    print(f"You rolled a {D12}!")
D14 = random.randint(1,14)
if dice == "D14":
    print(f"You rolled a {D14}!")
D16 = random.randint(1,16)
if dice == "D16":
    print(f"You rolled a {D16}!")
D18 = random.randint(1,18)
if dice == "D18":
    print(f"You rolled a {D18}!")
D20 = random.randint(1,20)
if dice == "D20":
    print(f"You rolled a {D20}!")
if gameaccept == "No":
    print("You were not willing to play with me, so now I have to sell your information to China.")
if gameaccept == "Yes":
    print("Thanks for playing with me, I will give you a ten percent less chance of being captured by China, and my respect.")

#I will store the dice variables right here
#D4 = random.randint(1,4)
#D6 = random.randint(1,6)
#D8 = random.randint(1,8)
#D10 = random.randint(1,10)
#D12 = random.randint(1,12)
#D14 = random.randint(1,14)
#D16 = random.randint(1,16)
#D18 = random.randint(1,18)
#D20 = random.randint(1,20)