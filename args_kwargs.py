#JR *args **kwargs notes

def hello(name, *args):
    print(args)
    for first in args:
        print(f"Hello{first}{name}")
hello(" Alex", " Katie", " Andrew", " Tia", " Treyson", " Xavier", " Jake")

hello(" Kringle", " Kris")

def clean(**kwargs):
    if not kwargs.get("data"):
        return "There is no data"
    elif kwargs.get("type") == "str":
        return kwargs.get("data").strip().lower()
    elif kwargs.get("type") == "int":
        return int(kwargs.get("type"))
    elif kwargs["type"] == "list":
        return str(f"{x}, " for x in kwargs["data"])
    elif kwargs["type"] == "bool":
        return f"{kwargs["data"]}"

print(clean(type="float", data="3.1415", decimals=3))
print(clean(data="utah", type = "str"))

def clean(type, data):
    if type == "str":
        return data.strip().lower()
    elif type == "int":
        return int(data)
    elif type == "float":
        return round(float(data), 2)
    elif type == "list":
        return str(f"{x}, " for x in data)
    elif type == "bool":
        return f"{data}"
    
print(clean(type="float", data="3.1415"))
print(clean(data="utah", type = "str"))