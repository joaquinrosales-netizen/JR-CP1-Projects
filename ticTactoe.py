# Tic Tac Toe Game or at least something I can use to help me on the actual assignment
print("Welcome to BlobGPT")
print("We are going to play tic tac toe!")
print("Get a second buddy to play with you!")
board = [" "] * 9
lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
         (0, 3, 6), (1, 4, 7), (2, 5, 8),
         (0, 4, 8), (2, 4, 6)]

def show_board():
    print(f" {board[0]} | {board[1]} | {board[2]}\n---+---+---\n"
          f" {board[3]} | {board[4]} | {board[5]}\n---+---+---\n"
          f" {board[6]} | {board[7]} | {board[8]}")

for turn in range(9):
    show_board()
    player = "X" if turn % 2 == 0 else "O"
    while True:
        move = input(f"Player {player}, Here are your options: A1, A2, A3, B1, B2, B3, C1, C2, C3: ").strip().upper()
        if len(move) == 2 and move[0] in "ABC" and move[1] in "123":
            spot = "ABC".index(move[0]) * 3 + int(move[1]) - 1
            if board[spot] == " ":
                board[spot] = player
                break
        print("That move isn't valid. Try a different one.")

    if any(all(board[spot] == player for spot in line) for line in lines):
        show_board()
        print(f"Player {player} wins!")
        break
else:
    show_board()
    print("It's a tie!")

print("Thanks for playing BlobGPT's Tic Tac Toe! (BlobGPT is not responsible for any arguments that may arise from this game, please play responsibly.A1)")