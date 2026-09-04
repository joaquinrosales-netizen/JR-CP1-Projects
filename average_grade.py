
# Joaquin Rosales Programming 1 Grade Average Assignment

print("How many classes do you have and what are they?")
periodone = input("What is your first period?")
periodtwo = input("What is your second period?")
periodthree = input("What is your third period?")
periodfour = input("Do you have lunch for fourth period or advisory?")
if periodfour == "lunch":
    print("Ok, so you have advisory for fifth period")
if periodfour == "advisory":
    print("Ok, so you have lunch for fifth period")
periodsix = input("What is your sixth period?")
periodseven = input("What is your seventh period?")
periodeight = input("What is your last period?")
print("Ok I am now going to ask you your grade in each of your classes")
onegrade = input("What is your grade in " + periodone + "?")
twograde = input("What is your grade in " + periodtwo + "?")
if twograde == "0":
    print("Ok, I won't mark that grade")
if twograde == "N/A":
    print("Ok, I won't mark that grade")
threegrade = input("What is your grade in " + periodthree + "?")
if periodfour == "lunch":
    print("I won't grade you for this")
if periodfour == "advisory":
    print("I will now ask you your grade in advisory, if you have a grade. If none, just type 0.")
fivegrade = input("What is your grade in advisory?")
sixgrade = input("What is your grade in " + periodsix + "?")
if sixgrade == "none":
    print("Ok, it's because it's seminary")
else:
    print("Ok")
sevengrade = input("What is your grade in" + periodseven + "?")
eightgrade = input("What is your grade in" + periodeight + "?")
classes = input("I will ask you, how many classes do you have that have grades?")
if periodfour == "advisory":
    print("Your average grade is: " + str((float(onegrade) + float(twograde) + float(threegrade) + float(sixgrade) + float(sevengrade) + float(eightgrade)) / float(classes)))
if periodfour == "lunch":
    print("Your average grade is: " + str((float(onegrade) + float(twograde) + float(threegrade) + float(sixgrade) + float(sevengrade) + float(eightgrade)) / float(classes)))
if twograde == "N/A":
    print("Your average grade is: " + str((float(onegrade) + float(threegrade) + float(sixgrade) + float(sevengrade) + float(eightgrade)) / float(classes)))
