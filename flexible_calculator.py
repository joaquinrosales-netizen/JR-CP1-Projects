#JR Flexible Calculator

def hello(num, *args):
    print(args)
    for first in args:
        print(f"Hello{num}{first}")
hello(" 1", "0", "1", "2", "3", "4", "5", "6", "7")