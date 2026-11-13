#JR Combat Program CS1
import random

random_thingy = random.randint(1,100)
random_thingy1 = random.randint(1,100)
random_thingy2 = random.randint(1,100)
random_thingy3 = random.randint(1,100)
random_thingy4 = random.randint(1,100)


print("So basically")
print("Your a farmer")
print("And wolves are attacking your livestock")
print("And your too poor to hire people to get rid of the wolves")
print("And your too lazy to get more shells for your shotgun")
print("So you just send three of your animals to fight the wolves")
print("No real animals have been harmed")

name = input("What is your name?: ").strip().title()

pig_health = 90
pig_atttack = 20

chicken_health = 40
chicken_attack = 40

cow_health = 150
cow_attack = 10

print("The enemy, Wolf stats, Health:120, Damage: 40")

print("Pig Stats, Health:90, Damage:20")
print("Chicken stats, Health:40, Damage:40")
print("Cow Stats, Health:150, Damage:10")

print("IMPORTANT INFORMATION: There is a random damage system, so all attacks either do normal damage or lower damage. You only have three full health heals, and you can use them whether the animal is dead or not")

heals = 3
heals_minus_one = 2
heals_minus_two = 1
heals_none_left = 0

choice = input("The time comes to end the wolves' reign of terror once in for all, Who are you choosing first? (try not to let the animals die): ").strip().title()

while True:
    if choice == "Pig":
       active_choice = input("Good choice, the wolf has arrived, here are your options\nFight\nHeals\nSwitch\nGive up ").strip().title()
    if active_choice == "Give up".strip().title():
        print("Wow, your really just gonna end it like that.")
        print("Say bye to your animals I guess")
        break
    elif active_choice == "Fight":
        if random_thingy < 50:
            print("hi")

    elif choice == "Chicken":
        active_choice = input("Good choice, the wolf has arrived, here are your options\nFight\nHeals\nSwitch\nGive up ").strip().title()

    elif choice == "Cow":
       active_choice = input("Good choice, the wolf has arrived, here are your options\nFight\nHeals\nSwitch\nGive up ").strip().title()

    else:
        print("Invalid, try again")
    break

