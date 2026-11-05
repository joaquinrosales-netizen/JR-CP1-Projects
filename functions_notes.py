# JR functions notes

#parameters that are needed
name = input("What is your name?: ")
attempts = 0

def increase():
    return attempts

def poopy(name, age = 35):
    print("poop ha ha")
    print("poopypants")
    print(f"Happy birthday dear {name}! poopypants")
    print(f"You are now {age} years old!")

def stupid_proof(user_answer, correct):
    user_answer = user_answer.strip().title()
    if user_answer in correct:
        return True, user_answer, attempts + 1
    else:
        return False, user_answer, attempts + 1

print("November")
poopy("Tia", 30) 
print("December")
poopy("Xavier", 24)
print("January")
poopy("Treyson", 20)
print("June")
poopy(name, 14)

while True:
    capital = input("What's the capital of Utah: ")
    correct, capital, attempts = stupid_proof(capital, ["Salt Lake City", "Slc", "Salt Lake"])
    if correct:
        print(f"Good job {capital} is the capital of Utah.")
        break
    else:
        print(f"Wrong, {capital} is not the capital of Utah")   