from ultimateBoard import UltimateBoard
from board import Board
from minimaxagent import MinimaxAgent
from alphabeta import AlphaBetaAgent

class Runner:
    'Runner for Tic Tac Toe game'
    
    def __init__(self):
        self.board=UltimateBoard()
        self.agent=AlphaBetaAgent(1, 1, 'y', 'x', 2.5)
        self.agent2=MinimaxAgent(1, 1, 'x', 'y', 4)
        
    def printBoard(self):
        largeArr=self.board.largeBoard
        print( "       0        1        2     ")
        print("    _______  _______  _______  ")
        for i in range(3):
            row1="  || "
            row2=str(i)+" || "
            row3="  || "
            for j in range(3):
                localArr=largeArr[i][j].boardM
                for k in range(3):
                    row1=row1+localArr[0][k]
                    row2=row2+localArr[1][k]
                    row3=row3+localArr[2][k]
                    if k!=2:
                        row1=row1+"|"
                        row2=row2+"|"
                        row3=row3+"|"
                row1=row1+" || "
                row2=row2+" || "
                row3=row3+" || "
            print( row1)
            print( "  || ----- || ----- || ----- ||")
            print (row2)
            print ("  || ----- || ----- || ----- ||")
            print (row3)
            print ("  ||_______||_______||_______||")

    def doMoves(self):
        currentPlayer='x'
        otherPlayer='y'
        tempPlayer=''
        self.printBoard()
        print ("It is "+currentPlayer+"'s turn")
        x=int(input('Enter starting x location '))
        y=int(input('Enter starting y location '))
        currentBoard=(x, y)
        while self.board.winner=="N":
            self.printBoard()
            if currentPlayer=='y':
                move=self.agent.analyze(self.board, currentBoard, 0, -999999, 999999)
                loc=move
                self.board.move(currentPlayer, currentBoard[0], currentBoard[1], loc[0], loc[1])
                x=loc[0]
                y=loc[1]
            else:
                move=self.agent2.analyze(self.board, currentBoard, 1, 'x', 'y')
                loc=move
                self.board.move(currentPlayer, currentBoard[0], currentBoard[1], loc[0], loc[1])
                x=loc[0]
                y=loc[1]
            winner=self.board.checkWinner()
            while self.board.smallBoard.boardM[x][y]!='.':
                if currentPlayer=='y':
                    loc=self.agent2.analyze(self.board, currentBoard, 1, 'x', 'y')
                    x=loc[0]
                    y=loc[1]
                else:
                    #Call the analyze function to pick the best board for y to play in
                    loc=self.agent.analyze(self.board, currentBoard, 0, -999999, 999999)
                    x=loc[0]
                    y=loc[1]
            tempPlayer=currentPlayer
            currentPlayer=otherPlayer
            otherPlayer=tempPlayer
            tempPlayer=""
            currentBoard=(x, y)
        print( "Congratulations player "+self.board.winner+" you have won the game!")
        self.printBoard()
            

runner=Runner()
runner.doMoves()
            
        
