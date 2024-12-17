from collections import deque

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
        move = int(move) - 1
        row = move // 3
        col = move % 3
        if board[row][col] == " ":
            board[row][col] = "X"
            break
        else:
            print("Invalid move. Try again.")

def bfs(board, player):
    queue = deque([(board, player)])
    while queue:
        current_board, current_player = queue.popleft()
        if check_win(current_board, "O"):
            return 1
        elif check_win(current_board, "X"):
            return -1
        elif check_draw(current_board):
            return 0
        next_player = "O" if current_player == "X" else "X"
        for i in range(3):
            for j in range(3):
                if current_board[i][j] == " ":
                    new_board = [row[:] for row in current_board]
                    new_board[i][j] = current_player
                    queue.append((new_board, next_player))

def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = bfs(board, "X")
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = "O"

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
    #bfs que fisrt in first out
    #dfs stack last in first out