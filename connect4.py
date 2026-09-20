ROWS = 6
COLS = 7

def create_board():
	board = []

	for row in range(ROWS):
		board.append([" "] * COLS)

	return board


def draw_board():
	print("\033[2J\033[H", end="")
	print("CONNECT FOUR")
	print("==============")
	for row in board:
		print("|", end="")
		for cell in row:
			print(f" {cell} |", end="")
		print()
	print("  1   2   3   4   5   6   7")


def check_winner(player):
	for row in range(ROWS):
		for col in range(COLS-3):
			if (board[row][col] == player and
				board[row][col + 1] == player and
				board[row][col + 2] == player and
				board[row][col + 3] == player):
				return True
	for row in range(ROWS-3):
		for col in range(COLS):
			if (board[row][col] == player and
				board[row + 1][col] == player and
				board[row + 2][col] == player and
				board[row + 3][col] == player):
				return True
	for row in range(ROWS - 3):
		for col in range(COLS - 3):
			if (board[row][col] == player and
				board[row + 1][col + 1] == player and
				board[row + 2][col + 2] == player and
				board[row + 3][col + 3] == player):
				return True
	for row in range(ROWS - 3):
		for col in range(3, COLS):
			if (board[row][col] == player and
				board[row + 1][col - 1] == player and
				board[row + 2][col - 2] == player and
				board[row + 3][col - 3] == player):
				return True
	return False

while True:
	board = create_board()
	current_player = "X"

	draw_board()

	while True:
		try:
			column = int(input(f"Player {current_player}, choose a column: "))
		except ValueError:
			print("Please enter a number.")
			continue
		if column <1 or column > 7:
			print("Please choose a column from 1 to 7.")
			continue

		piece_placed = False

		for row in range(ROWS - 1, -1, -1):
			if board[row][column - 1] == " ":
				board[row][column - 1] = current_player
				piece_placed = True
				break

		if piece_placed and check_winner(current_player):
			draw_board()
			print(f"Player {current_player} wins!")
			break

		if " " not in board[0]:
			draw_board()
			print("It's a draw!")
			break

		if piece_placed:
			draw_board()
			print(f"Player {current_player} placed in column {column}!")

			if current_player == "X":
				current_player = "O"
			else:
				current_player = "X"

	again = input("Play again? (y/n): ")

	if again.lower() != "y":
		break

