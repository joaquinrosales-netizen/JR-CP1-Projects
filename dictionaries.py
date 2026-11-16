#JR Dictionary notes

# Collection of key and value pairs

car = {
    "make": "jeep",
    "modle": "Wrangler",
    "color": "silver",
    "year": 2023
}
keys = list(car.keys())
values = list(car.values())
for key in keys:
    print(f"{key} is {car[key]}")

print(values)
print(len(car))
if "transmission" in car:
    print(car["transmission"])
else:
    car["transmission"] = "automatic"

car.pop("color")
for key in keys:
    print(f"{key} is {car[key]}")

avatar = {
    "Water": {
        "Katara": "Water Bender",
        "Sokka": "Leader",
    }
}

print(avatar.Water.Katara)

"Earth":{
    "Toph": "something"
} #type: ignore