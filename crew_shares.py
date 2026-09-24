#Unit 2 final project Joaquin Rosales
import random
def main():
    crew = input("How many crew members do you have?: ")
    crew_members = crew - 2
    units = random.randint(500, 5000)
    print(f"All crew members: {crew_members}")
    print(f"Units: {units}")
    crew_payment = crew_members * 3
    units_left = units - crew_payment
    yondu_share = round(units_left * 0.13, 2)
    units_left = units_left - yondu_share
    quill_share = round(units_left * 0.11, 2)
    units_left = units_left - quill_share
    last_share = round(units_left /crew_members,2 )
    yondu_total = yondu_share + last_share
    quill_total = quill_share + last_share
    crew_per_person = 3 + last_share
    print(f"Yondu's 13% payment: {yondu_share} units")
    print(f"Quill's 11% payment: {quill_share} units")
    print(f"Final split per person: {last_share} units")
    print(f"Yondu: {yondu_total:.2f} units")
    print(f"Quill: {quill_total:.2f} units")
    print(f"Every crew member: {crew_per_person:.2f} units")
    print(f"Final split per person: {last_share} units")
    print(f"Yondu: {yondu_total:.2f} units")
    print(f"Quill: {quill_total:.2f} units")
    print(f"Every crew member: {crew_per_person:.2f} units") 