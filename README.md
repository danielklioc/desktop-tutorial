# Welcome to GitHub Desktop!

In-Tic-Tac-Toe-Ception

Tic-tac-toe
Tic-tac-toe is a simple, 2-player, strategy game played on a board of 9 cells set out in a 3x3 square.  The first player places an "X" an any cell.  The second player places an "0" in any remaining cell.  The players continue taking turns placing their mark in remaining cells.  The winner is the first player to place three of his marks in a row, column, or diagonal.

TIC-TAC-TOE-CEPTION

Tic-tac-toe-ception is a 2-player computer game played on a game board comprising nine tic-tac-toe games set out in nine mini-squares within a 3x3 greater-square.  Thus, there are 81 cells, arranged in nine 3x3 mini-squares within a greater square.

Objective:
The objective of this game is to be the first to win three tic-tac-toe games lying in a row, column, or diagonal within the greater-square.

Rules of Play:
1.  The first player may place an "X" in any cell within any mini-square on the board.  
2.  The selected cell position within this mini-square corresponds to the mini-square position within the greater-square where the second player must then place an "O".
3.  Thereafter, the two players take turns placing their mark in any unfilled cell within the mini-square dictated by the cell position marked by the previous player.  For the first player, this mini-square will be outlined in red.
4.  (variation A) The first tic-tac-toe winner in a mini-square remains the winner in that mini-square for the remainder of the game.
4. (variation B - currently not implemented) - Anytime you get 3 in a row in any mini board, you become a winner of that board. If the other player also gets 3 in a row in that board, either before or after they are then co-owners of the board with you.
5 (variation A).  If a player is sent to a mini-square in which all the cells are filled, the player may next place his mark in any unfilled cell in any other mini-board.
5 (variation B - current default).  If a player is sent to a mini-square that has already been won, or in which all the cells are already filled, then the player may next place his mark in any unfilled cell in any other mini-board.
5 (variation C - currently not implemented). If a player is sent to a mini-square that has already been won, they must play in that mini-square (if not empty), but then they get to go again.  If a player is sent to a totally filled square then they may go anywhere.
5 (variation D - currently not implemented). If a player is sent to a mini-square that has already been won, they must play in that mini-square (if not empty) but then they get to continue to keep control and continue to send themselves to other boards that have already been won until they send themselves and play in a board that has not yet been won.
 * 
 * AI discussion:
 * There are three different Bots now.  A random bot, which just plays randomly.  A monte carlo bot (which plays out as many random games as it can within 5 seconds and plays which ever next position had the greatest percentage of wins).  There is also a perfect bot, which if played as X should never lose under rule 5a.  Under 5b its strategy is very bad.
 * 
 * TODO: make Perfect Bot as "O" be perfect if "X" messes up under rule 5a. 
 * TODO: implement rule 5c
 * TODO: implement rule 5d
 * TODO: implement rule 4b
 * TODO: modify Monte to better detect when the next move might cause the opponent to win
 * TODO: when the number of a available moves left becomes small enough to be able to fully calculate out all possible future moves, consider doing this (though Monte might handle this just fine)
 * TODO: rearrange the code a bit to be able to reuse the same class for the large board and the mini-boards, and hence allow one more layer of recursion.  One possilbe rule of where you are forced to play is by keeping track of the last two moves.  The move two turns ago says which big board to play on. The move one turn ago says which mid-sized board to play on.
 * TODO: crazy long term idea is to allow an arbitrary depth of recursion and allow people to zoom in or out of the board. (please feel free to write a spin-off that does this so I don't have to spend another weekend doing it myself :)
 * 
 * Search space:
 * The first move of the game has 81 different possibilities.
 * After that the moves are constrained to a single board.
 * There will be 8 boards (the first board has one filled in
 * already) that have 9 choices when you first arrive. After
 * that there will 9 board with 8 choices, 9 with 7 choices,
 * 9 with 6, etc, until you are forced to move in the last
 * spot. So at the beginning of the game there will be:
 * 81*9^8*8^9*7^9*6^9*5^9*4^9*3^9*2^9 = 9.8*10^50 ways to
 * randomly fill in the whole board. Many paths will win the
 * game early, so the actual search space will be less than
 * this, but as you can see the number would still be way to
 * big to brute force.
 