import random

def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def get_available_moves(board):
    return [i for i in range(9) if board[i] == " "]

def minimax(board, is_maximizing):
    player = "O" if is_maximizing else "X"
    opponent = "X" if is_maximizing else "O"

    if check_winner(board, opponent):
        return -1 if is_maximizing else 1
    if " " not in board:
        return 0

    best = -float("inf") if is_maximizing else float("inf")
    for move in get_available_moves(board):
        board[move] = player
        score = minimax(board, not is_maximizing)
        board[move] = " "
        best = max(best, score) if is_maximizing else min(best, score)
    return best

def ai_move(board, difficulty):
    if difficulty == "easy":
        return random.choice(get_available_moves(board))
    else:
        best_score = -float("inf")
        best_move = None
        for move in get_available_moves(board):
            board[move] = "O"
            score = minimax(board, False)
            board[move] = " "
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

def get_player_move(board, name):
    while True:
        try:
            move = int(input(f"{name}, enter your move (0-8): "))
            if move in get_available_moves(board):
                return move
            else:
                print("❌ Invalid move. Available moves:", get_available_moves(board))
        except ValueError:
            print("⚠️ Please enter a valid number between 0 and 8.")

def play_game():
    print("🎮 Welcome to Tic-Tac-Toe!")
    mode = input("Choose mode: (1) Player vs AI or (2) Player vs Player: ")

    if mode == "1":
        player1 = input("Enter your name: ").strip() or "Player 1"
        player2 = "Computer 🤖"
        difficulty = input("Choose AI difficulty (easy/hard): ").strip().lower()
    else:
        player1 = input("Enter name for Player X: ").strip() or "Player X"
        player2 = input("Enter name for Player O: ").strip() or "Player O"
        difficulty = None

    symbols = {"X": player1, "O": player2}
    scores = {player1: 0, player2: 0, "Draws": 0}

    while True:
        board = [" "] * 9
        current_symbol = "X"
        print_board(board)

        while True:
            name = symbols[current_symbol]
            if name == "Computer 🤖":
                print(f"{name} is thinking...")
                move = ai_move(board, difficulty)
            else:
                move = get_player_move(board, name)

            board[move] = current_symbol
            print_board(board)

            if check_winner(board, current_symbol):
                print(f"🎉 {name} wins!")
                scores[name] += 1
                break
            elif " " not in board:
                print("😐 It's a draw!")
                scores["Draws"] += 1
                break

            current_symbol = "O" if current_symbol == "X" else "X"

        print("\n🏆 Current Scores:")
        for p, s in scores.items():
            print(f" - {p}: {s}")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! Final scores:")
            for p, s in scores.items():
                print(f" - {p}: {s}")
            break

if __name__ == "__main__":
    play_game()
