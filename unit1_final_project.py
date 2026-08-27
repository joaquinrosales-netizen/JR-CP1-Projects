#Unit 1 Final Joaquin Rosales
print("Welcome to the program user")
name = input("Whats your name user")
print("Ok, " + name + " I hope you are doing well.")
food = input("What is your favorite food")
print("Nice, I can't eat " + food + " Because I am a program, but any human can!")
superhero = input("Who is your favorite superhero")
if superhero == "Spider-man":
	print("Hey, Spideys my favorite too!")
else:
	print("Nice, that is a cool superhero!")
age = int(input("Finnaly, how old are you?"))
if age < 18:
	print("Bro's childhood is cocomelon")
if age > 18:
	print("Did you know the stegasorous, you ancient bloke? Bro went to class with cleopatra lol")
print("Anyway, " + name + " I have a job for you")
print("I want you to get me the best " + food + " ever")
quest=input("Do you accept " + str(name) + " ?")
if quest == "no":
	print("Darn it, go away if your too lazy then!")
if quest == "yes":
	print("Mmm, thanks for the meal!")
if quest == "Aren't you a program?":
	print("Oh yeah my bad")