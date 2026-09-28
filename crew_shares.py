import random

crew = int(input("How many members are in your crew?: "))

units = random.randint(500,5000)
print("Number of units: " + str(units))

lower_crew = crew - 2

yondu_share = round(units * 0.13)
quill_share = round(units * 0.11)

units_remaining = units - yondu_share
units_left = units_remaining - quill_share

final_split = round(units_left / lower_crew)

print("Yondu: " + str(yondu_share))
print("Quill: " + str(quill_share))
print("The Crew: " + str(final_split))