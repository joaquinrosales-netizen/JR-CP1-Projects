# JR Order up Joaquin Rosales

subway_menu = {
    "Sandwhiches": "BMT,Meatball Pepperoni,Subway Club,Grilled Chicken,Steak Philly,Veggie Delite,",
    "Sandwhiches": 8,
    "Chips": "Lays,Sunchips,Doritos,Cheetos,BBQ",
    "Chips": 1.5,
    "Cookies": "Chocolate Chip,Double Chocolate,Oatmeal Raisin,White Chip Macadamia",
    "Cookies": 1,
    "Drinks": "Pepsi, Pepsi Zero, Mountain Dew,Gatorade,Lemonade",
    "Drinks": 2.5,
    "Salad": "Honey Mustard,Grilled Chicken,All American Club,Tuna",
    "Salad": 10,
}
keys = list(subway_menu.keys())
values = list(subway_menu.values())
for key in keys:
    print(f"{key} is {subway_menu[key]}")
