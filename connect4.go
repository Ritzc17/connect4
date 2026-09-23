package main

type Piece string

const (
	Empty Piece = ""
	X     Piece = "X"
	O     Piece = "O"
)

type GameStatus string

const (
	InProgress GameStatus = "in_progress"
	XWon       GameStatus = "x_won"
	OWon       GameStatus = "o_won"
	Draw       GameStatus = "draw"
)

type Game struct {
	Board  [6][7]Piece
	Turn   Piece
	Status GameStatus
}

func main() {

}
