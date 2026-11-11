#JR Nesting Notes

win = False
text = True

if win:
    if text:
        print("Hallelujah")
    else:
        print("Try again")
else:
    print("You failed")

win = ["5","6","7"]

for won in win:
    print(won)
    for x in range(4):
        print("hugos mom")

names = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]

while True:
    for name in names:
        print(f"{name} LaRose")
    again = input("Do you need to see them again?: ")
    if again.lower() == "yes":
        pass
    else:
        break