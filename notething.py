# string notes or something

# strings are a collection of characters held together by quotation marks

#name = "Joaquin"

#age = "15"

#print(age + "2")

#print(name+" "+age)

#first_name = "Joaquin"
#last_name = "Rosales"
#full_name = first_name + " " + last_name
#print(full_name)

#sentence = 'then he said \n"That isn\'t fair"'
#print(sentence)

#print(full_name * 4)
#sentence = "The quick brown fox jumps over the lazy dog."
#print(sentence)
#print(sentence.find("w"))
#print(sentence[9:13])
#word = input("What word do you want?")
#start = sentence.find(word)
#length = len(word)
#print(sentence[start:start+length])

#another set of notes i guess
#JR, String methods

sentence = "The quick brown fox jumps over the lazy dog"

fixed = sentence.replace("fox", "wolf")

#name = input("What is your name").strip().title()

print(sentence.find("over"))

#we are trying to do ask the user their name here

first_name = input("What is your first name: ").strip().title()
last_name = input("What is your last name: ").strip().title()
first_seperated = first_name.split()
fixed = "".join(first_seperated)
last_seperated = last_name.split()
last_fixed = "".join(last_seperated)
full_name = fixed.title() + " " + last_fixed.title()
print("Hello " + full_name.title())
print(full_name.isalpha())
print(full_name.isnumeric())
print(full_name.isupper())


word = input("What word do you want?: ").strip().lower()
new_word = input("What will replace it: ").strip().lower()

location = sentence.find(word)
new_sentence = sentence.replace(word,new_word)
print(new_sentence)
print(sentence.find("over"))

print(sentence.split("the"))

#print(sentence.lower())
#print(sentence.upper())
#print(sentence.capitalize())
#print(sentence.title())
#print(fixed)

#print("Welcome to BlobGPT")
#name = input("Please register your full name into the program: ")
#print("Hello " + name.strip().title())
