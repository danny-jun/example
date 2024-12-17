def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            row = move // 3
            col = move % 3
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Invalid move. The cell is already occupied. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = "O"

def minimax(board, is_maximizing):
    if check_win(board, "O"):
        return 1
    elif check_win(board, "X"):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)
        player_move(board)
        if check_win(board, "X"):
            print_board(board)
            print("Player wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_move(board)
        if check_win(board, "O"):
            print_board(board)
            print("AI wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
