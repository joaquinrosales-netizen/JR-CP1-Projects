# JR shopping list manager

shopping = []

while True:
    action = input("What would you like to add to the shopping list?: ")
    shopping.append(action)

    print(*shopping)

    if action == "remove":
        print(*shopping)
        remove = input("Which ones would you like to remove?: ")
        shopping.remove(*action)