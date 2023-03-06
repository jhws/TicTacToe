def draw_board(board):
    """
    This function draws the Tic Tac Toe board.
    """
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print()
        print("-------------")

def get_move(board, player):
    """
    This function gets the player's move and updates the board accordingly.
    """
    while True:
        try:
            move = input(f"Player {player}, please enter your move (row, column): ")
            row, col = map(int, move.split(","))
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("That space is already taken. Please try again.")
        except:
            print("Invalid move. Please try again.")
            
def check_win(board):
    """
    This function checks whether a player has won the game or not.
    """
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        # Check columns
        elif board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    # Check for tie
    elif " " not in board[0] and " " not in board[1] and " " not in board[2]:
        return "tie"
    else:
        return None

def play_game():
    """
    This function starts and plays the Tic Tac Toe game.
    """
    # Initialize the board
    board = [[" ", " ", " "] for i in range(3)]
    draw_board(board)
    # Start the game
    player = "X"
    while True:
        # Get the player's move
        get_move(board, player)
        # Draw the updated board
        draw_board(board)
        # Check if the game is over
        winner = check_win(board)
        if winner:
            if winner == "tie":
                print("It's a tie!")
            else:
                print(f"Player {winner} has won the game!")
            break
        # Switch to the other player
        if player == "X":
            player = "O"
        else:
            player = "X"

# Start the game
play_game()
