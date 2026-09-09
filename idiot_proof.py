print("Welcome to BlobGPT")
print("WARNING: If you type something invalid the program will stop working and you will have to start over")
print("Also by using me you agree to the terms and contitions of BlobGPT, which is monitored by BRICS, kapisch?")
first_name = input("Please register your first name into the program: ").capitalize().strip()
last_name = input("Please register your last name into the program: ").capitalize().strip()
full_name = first_name + " " + last_name
print("Hello " + full_name)
while True:
	try:
		GPA = float(input("What is your GPA? "))
		break
	except ValueError:
		print("Uhhh, I do not understanding. Please enter a number.")
while True:
	phone = input("Please register your phone number into the program: ").strip()
	if len(phone) == 10 and phone.isdigit():
		break
	print("I no understanding either. Please enter a valid ten-digit phone number. ")
print("Thank you for registering your information into the program. Your information is as follows:")
print("Name: " + full_name)
print("GPA: " + str(GPA))
print("Phone Number: " + phone)
print("I have eaten well, I totally won't sell your information to China, trust broskie. Have a good day :)")
