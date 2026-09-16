# Debugger wow :D Joaquin Rosales

grades = [85, 90, 78, 92, 88]

total = 0
count = 4

for grade in grades:
    total = total + grade

average = total / count

print(f"The average grade is: {average}")

scores = [12,45,7,68,33,90,21]

running_total = 0
highest_score = 0

for score in scores:
    running_total += score
    if score > highest_score:
        highest_score = score

average = running_total / len(scores)

print(f"The average score is: {average}")
print(f"The highest score is: {highest_score}")
