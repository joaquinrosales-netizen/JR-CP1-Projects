# Tic Tac Toe Game or at least something I can use to help me on the actual assignment
print("Welcome to BlobGPT")
print("We are going to play tic tac toe!")
print("Get a second buddy to play with you!")
board = ( "   |   |   \n"
          "   |   |   \n"
          "   |   |   \n"
          "-----------\n"
          "   |   |   \n"
          "   |   |   \n"
          "   |   |   \n"
          "-----------\n"
          "   |   |   \n"
          "   |   |   \n"
          "   |   |   \n")
print(board)
print("This is what the board will look like.")
print("Player one will be X and player two will be O")
print("The options you have are A1,A2,A3,B1,B2,B3,C1,C2,C3")
print("Ready, Start!")
playeronefirstmove = input("Player one, enter your move: ").capitalize().strip()
if playeronefirstmove == "A1":
    board = ( "   |   |   \n"
              " X |   |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n")

    print(board)
    print("Player two, your options are A2,A3,B1,B2,B3,C1,C2,C3")
if playeronefirstmove == "A2":
    board = ( "   |   |   \n"
              "   | X |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n")
    print(board)
    print("Player two, your options are A1,A3,B1,B2,B3,C1,C2,C3")

if playeronefirstmove == "A3":
    board = ( "   |   |   \n"
              "   |   | X \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n")
    print(board)
    print("Player two, your options are A1,A2,B1,B2,B3,C1,C2,C3")

if playeronefirstmove == "B1":
    board = ( "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              " x |   |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n") 
    print(board)
    print("Player two, your options are A1,A2,A3,B2,B3,C1,C2,C3")
if playeronefirstmove == "B2":
    board = ( "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   | x |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n")
    print(board)
    print("Player two, your options are A1,A2,A3,B1,B3,C1,C2,C3")
if playeronefirstmove == "B3":
    board = ( "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   |   | x \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n")
    print(board)
    print("Player two, your options are A1,A2,A3,B1,B2,C1,C2,C3")
if playeronefirstmove == "C1":
    board = ( "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              " x |   |   \n"
              "   |   |   \n")
    print(board)
    print("Player two, your options are A1,A2,A3,B1,B2,B3,C2,C3")
if playeronefirstmove == "C2":
    board = ( "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   | x |   \n"
              "   |   |   \n")
    print(board)
    print("Player two, your options are A1,A2,A3,B1,B2,B3,C1,C3")
if playeronefirstmove == "C3":
    board = ( "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   |   |   \n"
              "   |   |   \n"
              "-----------\n"
              "   |   |   \n"
              "   |   | x \n"
              "   |   |   \n")
    print(board)
    print("Player two, your options are A1,A2,A3,B1,B2,B3,C1,C2")
playertwofirstmove = input("Player two, please make your move: ").capitalize().strip()