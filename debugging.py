# Ravager Snack Bar
import random
#I customized some of the stuff just because :)
print("Welcome to BlobGPt")
print("We are PIRATES NOW! ARRRR!")
pirate_name = input("Arrr, what be yer name, matey? ").strip().title()
snack_name = input("Arrr, what snack be ye cravin', matey? ").strip().title()

price = random.randint(2, 8)
quantity = int(input("Arrr, how many would ye be wantin’, matey? "))

#I added the int in there because I want to make sure the quantity is a number and not the string

total = price * quantity

discounted_total = total - (total * 0.10)

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Arrr, " + pirate_name + "! Here be yer order summary:")
print("Snack: " + snack_name)
#it is not snackName, it is snack_name
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(discounted_total) + " credits")
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits")
#Parentheses missing right here (I already fixed it)                 ^
print("Arrr, thank ye for yer order!")
print("BlobGPT is monitored by China, BlobGPT does not speak in pirate english, BlobGPT does not condone piracy or other crimes commited against government, crimes including piracy will be punished by law.")