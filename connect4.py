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
