# UltimateTicTacToe
A command line version of Ultimate Tic Tac Toe including an ai variant

Use:

This program is designed to be run in the command line. It supports either python 2 or 3 (scripts for either are available.)
Runners currently support player vs player (ultRunner.py) player vs. AI (ultRunAI.py, currently uses the alpha beta pruning AI implementation, although both AI's are compatible and requires only the change of which class is defined).
There is also a runner for regular tic tac toe player vs player (runner.py).

Game play:

The first player selects their square. Currently there is no input sanitization so inputing any number higher than 3 or less than 1 will cause an error (this is a TODO). Squares are always selected by inputing the row, then the column. After the player selects their first large square, they select a smaller interior square. Game play continues in this way. A player who is sent to a square which is already completed is instructed to select a square to play in. (Known bug, occasionaly when the AI is sent to such a square it will overflow. This occurs rougly 5-10% of the time such an instance occurs, but does seem to be more common in the very late game. This is being worked on). When a player wins the game a message will be printed out in congratulations.

Author:

This program was created by James Gilkeson, an undergraduate student in the Drexel University college of computing and informatics. It was created to experiment with various AI methods as well as to create a simple command line game to waste time with. The author can be contacted at james@jameshsg.com.

Contributions

Anyone is welcome to branch this and develop their own AI algorithms and scoring methods, or to create a different board.