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
	if piece_placed:
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
