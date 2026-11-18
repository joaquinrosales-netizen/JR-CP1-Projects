# JR Order up Joaquin Rosales

reciept = []

subway_menu = {
    "Sandwiches": {
        "items": "BMT, Meatball Pepperoni, Subway Club, Grilled Chicken, Steak Philly, Veggie Delite",
        "price": 8
    },
    "Chips": {
        "items": "Lays, Sunchips, Doritos, Cheetos, BBQ",
        "price": 1.5
    },
    "Cookies": {
        "items": "Chocolate Chip, Double Chocolate, Oatmeal Raisin, White Chip Macadamia",
        "price": 1
    },
    "Drinks": {
        "items": "Pepsi, Pepsi Zero, Mountain Dew, Gatorade, Lemonade",
        "price": 2.5
    },
    "Salad": {
        "items": "Honey Mustard, Grilled Chicken, All American Club, Tuna",
        "price": 10
    }
}

keys = list(subway_menu.keys())
values = list(subway_menu.values())
for key in keys:
    print(f"{key}{subway_menu[key]}")

while True:
    print(keys)
    menu_order = input("Which menu would you like to see?: ").strip().title()

    if menu_order == "Sandwiches":
        print(subway_menu["Sandwiches"])
        amount = input("How many sandwhiches would you like?: ") 
        order = input("Which sandwhiches would you like?")
        reciept.append(order)
        print(reciept)
        
    if menu_order == "Chips":
        print(subway_menu["Chips"])
        amount = input("How many Chips would you like: ") 
        order = input("Which chips would you like?")
        reciept.append(order)
        print(reciept)