# Jr For Loops Notes
import time

# Iteration
siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]

for siblings in siblings:
    print(f"Good morning {siblings}!")


grades = [100, 87, 84, 53, 45, 78, 72, 88, 3, 94]
average = 0

for grade in grades:
    average += grade
    print(f"{grade} was added.")

average = average/len(grades)
print(f"The average grade is {average:.2f}.")

# If I do just (20), it will show 0 and only count to 19, but if I used this, it gives me what I want

for i in range(2,21,2):
    print(i)
    time.sleep(0.5)

for i in range(20, 1, -1):
    print(i)
    time.sleep(0.5)