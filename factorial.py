# Jr factorial calculator

num = int(input("What number do you want the factorial of?: "))

factorial = 1

for i in range(num, 0, -1):
    factorial = factorial * i
    print(i, end=" x " if i > 1 else "")

print(" =", factorial)