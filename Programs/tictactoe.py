def print_board(board):
    # Display the Tic-Tac-Toe board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check if the player has won
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    # Check if the board is full (a tie)
    return all(cell != " " for row in board for cell in row)

def play_tic_tac_toe():
    # Initialize the game
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))
        
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)
            
            if check_winner(board, current_player):
                print(f"Player {current_player} wins! Congratulations!")
                break
            elif is_board_full(board):
                print("It's a tie! Well played.")
                break
            
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

# Start the Tic-Tac-Toe game
play_tic_tac_toe()
