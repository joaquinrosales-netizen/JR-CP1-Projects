#JR multiplication table
numg = int(input("What size would you like the board to be? "))

for numg in range(1,numg):
    for num in range(1,30):
        print(numg * num, end=" ") 
    print()