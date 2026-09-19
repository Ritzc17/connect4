ROWS = 6
COLS = 7

board = []
for row in range(ROWS):
	board.append([" "] * COLS)

print("CONNECT FOUR")
print("==============")

for row in board:
	print("|", end="")
	for cell in row:
		print(f" {cell} |", end="")
	print()

print("  1   2   3   4   5   6   7")

current_player = "X"

while True:
	column = int(input(f"Player {current_player}, choose a column: "))
	for row in range(ROWS - 1, -1, -1):
		if board[row][column - 1] == " ":
			board[row][column - 1] = current_player
			break
	if current_player == "X":
		current_player = "O"
	else:
		current_player = "X"

	for row in board:
		print("|", end="")
		for cell in row:
			print(f" {cell} |", end="")
		print()

	print("  1   2   3   4   5   6   7")
