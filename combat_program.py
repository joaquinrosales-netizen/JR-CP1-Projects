#JR Combat Program CS1

print("So basically")
print("Your a farmer")
print("And wolves are attacking your livestock")
print("And your too poor to hire people to get rid of the wolves")
print("And your too lazy to get more shells for your shotgun")
print("So you just send three of your animals to fight the wolves")
print("No real animals have been harmed")

name = input("What is your name?: ").strip().title()

pig_health = 90
pig_attack = 20

chicken_health = 40
chicken_attack = 40

cow_health = 150
cow_attack = 10

wolf_health = 120
wolf_attack = 40

print(f"The enemy: Health:{wolf_health}, Damage:{wolf_attack} ")

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
        active_choice_pig = input("Good choice, the wolf has arrived, here are your options\nFight\nHeals\nSwitch\nCheck Health\nGive up ").strip().title()
        if active_choice_pig == "Check Health":
            print(f"Your pig is at {pig_health}")
        elif active_choice_pig == "Give Up":
            print("Wow, your really just gonna end it like that.")
            print("Say bye to your animals I guess")
            break
        elif active_choice_pig == "Fight":
            print("Attack hit!")
            wolf_health = max(0, wolf_health - pig_attack)
            print(f"The wolf is now at {wolf_health} health")
            pig_health = pig_health - wolf_attack
            print("The wolf attacks!")
            print(f"The pig is damaged! It is at {pig_health} HP!")
        elif active_choice_pig == "Heals":
            if heal_counter_pig > 0:
                pig_health += heal
                heal_counter_pig -= 1
                print(f"The pig healed! Health: {pig_health}")
            else:
                print("You already used your pig's heal!")
        elif active_choice_pig == "Switch":
            print("Commencing switch")
            continue
        if pig_health <= 0:
            print("Your pig is dead, sorry for the loss")
            continue


    elif choice == "Cow":
        active_choice_cow = input("Good choice, the wolf has arrived, here are your options\nFight\nHeals\nSwitch\nCheck Health\nGive up ").strip().title()
        if active_choice_cow == "Check Health":
            print(f"Your cow is at {cow_health}")
        elif active_choice_cow == "Give Up":
            print("Wow, your really just gonna end it like that.")
            print("Say bye to your animals I guess")
            break
        elif active_choice_cow == "Fight":
            print("Attack hit!")
            wolf_health = max(0, wolf_health - cow_attack)
            print(f"The wolf is now at {wolf_health} health")
            cow_health = cow_health - cow_attack
            print("The wolf attacks!")
            print(f"The cow is damaged! It is at {cow_health} HP!")
        elif active_choice_cow == "Heals":
            if heal_counter_cow > 0:
                cow_health += heal
                heal_counter_cow -= 1
                print(f"The cow healed! Health: {cow_health}")
            else:
                print("You already used your pig's heal!")
        elif active_choice_cow == "Switch":
            print("Commencing switch")
            continue
        if cow_health <= 0:
            print("Your cow is dead, sorry for the loss")
            continue

    elif choice == "Chicken":
        active_choice_chicken = input("Good choice, the wolf has arrived, here are your options\nFight\nHeals\nSwitch\nCheck Health\nGive up ").strip().title()
        if active_choice_chicken == "Check Health":
            print(f"Your chicken is at {chicken_health}")
        elif active_choice_chicken == "Give Up":
            print("Wow, your really just gonna end it like that.")
            print("Say bye to your animals I guess")
            break
        elif active_choice_chicken == "Fight":
            print("Attack hit!")
            wolf_health = max(0, wolf_health - chicken_attack)
            print(f"The wolf is now at {wolf_health} health")
            chicken_health = chicken_health - wolf_attack
            print("The wolf attacks!")
            print(f"The chicken is damaged! It is at {chicken_health} HP!")
        elif active_choice_chicken == "Heals":
            if heal_counter_chicken > 0:
                chicken_health_health += heal
                heal_counter_chicken -= 1
                print(f"The chicken healed! Health: {chicken_health}")
            else:
                print("You already used your chicken's heal!")
        elif active_choice_chicken == "Switch":
            print("Commencing switch")
            continue
        if chicken_health <= 0:
            print("Your chicken is dead, sorry for the loss")
            continue

        if wolf_health == 0:
            print("Congrats, you beat the wolf!")
            break

    else:
        print("Invalid, try again")
        continue
    # i need this to work