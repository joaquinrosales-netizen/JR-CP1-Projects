#Unit 1 Final Joaquin Rosales
print("Welcome to the program user")
name = input("Whats your name user")
print("Ok, " + name + " I hope you are doing well.")
food = input("What is your favorite food")
print("Nice, I can't eat " + food + " because I am a program, but any human can!")
superhero = input("Who is your favorite superhero")
if superhero == "Spider-man":
	print("Hey, Spideys my favorite too!")
else:
	print("Nice, that is a cool superhero!")
age = int(input("Finally, how old are you?"))
if age < 18:
	print("Bro's childhood is cocomelon")
elif age > 18:
	print("Did you know the stegasorous, you ancient bloke? Bro went to class with cleopatra lol")
else:
	print("YOU STINK OF RATS")
print("Anyway, " + name + " I have a job for you")
print("I want you to get me the best " + food + " ever")
quest=input("Do you accept " + str(name) + " ?")
if quest == "no":
	print("Darn it, go away if you're too lazy then!")
if quest == "yes":
	print("Mmm, thanks for the meal!")
if quest == "Aren't you a program?":
	print("Oh yeah my bad")
print("Ok, " + name + " I have had a great time with you, I leanred your favorite food is " + food + " I learned you are " + age + " years old, I learned your favorite superhero is" + superhero + " and I learned how willing you are to do things. So long " + name + " I'll just sit here in empty space forever.")