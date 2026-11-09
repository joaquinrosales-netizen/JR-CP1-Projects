#JR ceaser cypher encoder
def encode(message, shift):
    result = ""

# Determines the letter outputting and stuff and sees the capitalsj
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                start = ord('A')
            else:
                start = ord('a')

            new = chr((ord(letter) - start + shift) % 26 + start)
            result += new
        else:
            result += letter

    return result

#This is where the actual encoding starts, where it shifts the letters according to the user inputs. 
def decode(message, shift):
    return encode(message, -shift)
calculation = input("Choose operation (1 for encode, 2 for decode): ")

message = input("Enter the message: ")

message_changed = int(input("Enter the shift value: "))

if calculation == "1":
    result = encode(message, message_changed)
    print("Encoded message:", result)

elif calculation == "2":
    result = decode(message, message_changed)
    print("Decoded message:", result)

else:
    print("Invalid, try again.")