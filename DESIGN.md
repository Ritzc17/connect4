# Connect Four Go Rewrite - Design Document

## Goal

I want to take the connect4 game and add on network connectivity.
When the program is launched, a player can choose to either play locally (side by side) or Host or Join.
A Host player will wait for a connection. A Joining player will enter the IP address they want to join.
Players can give themselves names that will present in a multiplayer match.
Multiple matches can be played with players switching X and O every game, a running win count is displayed.

## Requirements

-Compiled executable requries no external runtime or third-party packages
-Functions entirely within a terminal
-Players connect to each other via TCP
-Supports local two-player play on a single machine
-Supports hosting or joining a network game
-Players can choose display names
-The host maintains the authoritative game state
-Invalid moves are rejected
-Both players see the same board state after every move
-Detects wins and draws
-Supports multiple games without reconnecting
-Alternates player pieces between games
-Maintains a win count for the duration of the session
-Handles a player disconnecting without crashing

## Non-Goals

-No in-game chat
-No matchmaking
-No persistent account/scores
-No security/hardening, assume all players are good actors

## Architecture

-The host acts as the authoritative game server
-The host maintains the canonical game state
-The joining player sends requested moves to the host
-The host validates moves, updates the game state, and sends the resulting state to both players
-Clients do not independently decide game outcomes.

### Establishing a Connection

Host:
1. Player selects Host
2. Player enters a display name
3. Program begins listening for a TCP connection
4. Program waits until another player connects.
5. Host may press X at any time to cancel listening and exit to main menu

Joiner:
1. Player selects Join
2. Player enters a display name
3. Player enters the host's IP address
4. Program attempts to establish a TCP connection with the host
5. Player may press X at any time to cancel attempted connection and exit to main menu

After Connection:
1. Host and joiner exchange display names
2. Both players are notified that the connection was successful
3. Game 1 begins
4. Host starts as X and takes the first move

## Game Flow
1. Player assigned to X takes the first move
2. Both players are shown an empty board
3. X submits a move
4. Host checks its validity, updates the game board
5. Both players are shown submitted moves and whether or not it was accepted
6. Game checks to see if placed piece is a winner
7. Play passes to O
8. Steps 3-7 repeat with play alternating between X and O
9. When game ends in a win or draw, both players are prompted to play again (y/n)
10. Answering Y will return the message "waiting for other player..." until both players have answered
11. Rematch occurs only if both players agree
12. N will immediately exit to main menu, other player receives "PLAYER_NAME has disconnected, press any key to return to main menu"
13. Typing "exit" as a move will end the game and disconnect both players

## Network Protocol

### Server Messages

NAME <name>
ASSIGN <X|O>
PLAY <X|O> <column>
TURN <X|O>
INVALID <reason>
WIN <X|O>
DRAW
SCORE <host_wins> <joiner_wins>
REMATCH
EXIT

### UI Messages

Player niko has connected!

You are now X

niko's turn to place X...

niko tries to place X at column 7, but it's full!

niko places an X at column 7!

'banana' is not a valid move, please enter a number

niko places an X at column 7 and wins the game!

Do you want to play again?

Waiting for niko to respond...

niko has quit the game! Press any key to return to main menu...

## Data Model

### Session State

Player names remain the same
Player total wins remain the same

### Game State

Which player is X and O
Contents of the game board
Whose turn it currently is
Game status - in prog, X won, O won, draw

## Proposed Go Types

### Player

Represents a player for the duration of a session

```go
type Player struct {
	Name string
	Wins int
}
```

Represents the current game state in a round

```go
type Game struct {
	board [6][7]string
	turn bool
	some way to show the status is in-progress, a winner, draw
}
```
