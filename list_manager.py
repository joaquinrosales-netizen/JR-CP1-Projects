shopping_list = []

while True:
    print("Welcome to BlobGPT")
    print("I own a grocery store now! And you are going to shop!")
    action = input("Here is your Shopping list. What would you like to do?\nAdd\nRemove\nView\nExit").strip().lower()
    print(action)

    if action == "Remove" and not shopping_list:
        print("Your shopping list is empty, you can not remove from your list.\n ")

    elif action == "add":
        added_item = input("What would you like to add to your list?: \n").strip().capitalize()
        shopping_list.append(added_item)

    elif action == "remove":
        removed_item = input("What would you like to remove?: \n").strip().capitalize()
        shopping_list.remove(removed_item)

    elif action == "view":
        print("Here is your shopping list:")
        print(shopping_list)
    
    elif action == "exit":
        print("Thank you for shopping with BlobGPT!")
        break

