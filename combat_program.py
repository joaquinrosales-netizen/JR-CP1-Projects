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

wolf_health = 120
wolf_attack = 40

print("The enemy, Wolf stats, Health:120, Damage: 40")

print("Pig Stats, Health:90, Damage:20")
print("Chicken stats, Health:40, Damage:40")
print("Cow Stats, Health:150, Damage:10")

print("IMPORTANT INFORMATION: There is a random damage system, so all attacks either do normal damage or no damage. You only have three full health heals, they restore health by 50 points, and you can use them whether the animal is dead or not, but only once for each animal, so choose carefully!")

heal = 50
heal_counter_pig = 1
heal_counter_chicken = 1
heal_counter_cow = 1

choice = input("The time comes to end the wolves' reign of terror once in for all, Who are you choosing first? (try not to let the animals die): ").strip().title()

while True:
    if choice == "Pig":
       active_choice_pig = input("Good choice, the wolf has arrived, here are your options\nFight\nHeals\nSwitch\nGive up ").strip().title()
    if active_choice_pig == "Give up".strip().title():
        print("Wow, your really just gonna end it like that.")
        print("Say bye to your animals I guess")
        break
    elif active_choice_pig == "Fight":
        if random_thingy < 50:
            print("Your attack missed!")
            pig_health_damaged = wolf_attack - pig_health
            print("The wolf has done 40 damage")
        elif random_thingy > 50:
            print("Attack hit!")
            wolf_pig = wolf_health - pig_atttack
            print(f"The wolf is now at {wolf_pig} health")
        elif pig_health_damaged == 50 and random_thingy1 < 50:
            pig_crit = wolf_attack - pig_health_damaged
            print(f"The pig is damaged by 50! It is at {pig_crit} HP!")
    elif active_choice_pig == "Heals":
        if pig_health == 90:
            pig_healed = pig_health + heal
            print("The pig is healed by 50!")
        elif pig_health_damaged == 50:
            pig_healed_two = pig_health_damaged + heal
            print("The pig is healed by 50!")

            
    elif choice == "Chicken":
        active_choice = input("Good choice, the wolf has arrived, here are your options\nFight\nHeals\nSwitch\nGive up ").strip().title()

    elif choice == "Cow":
       active_choice = input("Good choice, the wolf has arrived, here are your options\nFight\nHeals\nSwitch\nGive up ").strip().title()

    else:
        print("Invalid, try again")
        break