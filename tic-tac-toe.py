'''
Tic tac toe
Marielle Honey Chiong
'''


def main():
    player = next_player("")
    board = make_board()

    while not (game_win(board) or game_draw(board)):
        show_board(board)
        make_move(player, board)
        player = next_player(player)
    show_board(board)
    print("Well, wasn't that fun?")
    play_again()

def make_board():
    board = []
    for square in range(9):
        board.append(square+1)
    return board

def show_board(board):
    print(f"\n{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}\n")

def game_win(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def game_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def play_again():
    play = input("Do you want to play again (Y/N)? ")
    if "y" in play.lower():
        main()
    elif "n" in play.lower():
        print("Thanks for playing!")

if __name__ == "__main__":
    main()