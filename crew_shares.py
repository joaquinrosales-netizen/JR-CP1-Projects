import random

def main():
    total_pirates = int(input("How many pirates are on the ship, including Yondu and Quill? "))
    
    crew_members = total_pirates - 2
    
    total_units = random.randint(500, 5000)
    print(f"Total pirates: {total_pirates}")
    print(f"Total units generated: {total_units}")
    
    original_crew_payout = crew_members * 3
    units_left = total_units - original_crew_payout
    
    yondu_share = round(total_units * 0.13, 2)
    units_left = units_left - yondu_share
    
    peter_share = round(units_left * 0.11, 2)
    units_left -= peter_share
    
    final_split_per_person = round(units_left / total_pirates, 2)
    
    yondu_total = yondu_share + final_split_per_person
    peter_total = peter_share + final_split_per_person
    crew_individual_total = 3 + final_split_per_person
    
    print(f"Original payout to the crew: {original_crew_payout} units total")
    print(f"Yondu's 13%: {yondu_share} units")
    print(f"Peter's 11%: {peter_share} units")
    print(f"Final split per person: {final_split_per_person} units")
    
    print(f"Yondu Udonta: {yondu_total:.2f} units")
    print(f"Peter Quill: {peter_total:.2f} units")
    print(f"Each Crew Member: {crew_individual_total:.2f} units")

if __name__ == "__main__":
    main()