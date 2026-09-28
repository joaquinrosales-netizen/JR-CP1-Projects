#JR notes

age = 15
license = True

if age >= 18:
    print("You are an adult and can vote! Also you are depressed all the time and have a horrible boss.")
elif age >= 15 and license:
    print("You can drive! But you still have to go to school, loser")
elif age >= 15 and not license:
    print("You Could drive, but you don't have the paperwork, noob, go back to school school iz kool")
else:
    print("You are a minor, go to school, twerp, stupid kid")


win = False
hp = 10

if win or hp <= 0:
    print("Game Over")
    if hp > 0:
        pass
    else:
        print("You win!")
else:
    print("The game is still going")