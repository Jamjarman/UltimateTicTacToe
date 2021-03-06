from ultimateBoard import UltimateBoard
from board import Board

class Runner:
    'Runner for Tic Tac Toe game'
    
    def __init__(self):
        self.board=UltimateBoard()
        
    def printBoard(self):
        largeArr=self.board.largeBoard
        print "       0        1        2     "
        print "    _______  _______  _______  "
        for i in xrange(3):
            row1="  || "
            row2=str(i)+" || "
            row3="  || "
            for j in xrange(3):
                localArr=largeArr[i][j].boardM
                for k in xrange(3):
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
            print row1
            print "  || ----- || ----- || ----- ||"
            print row2
            print "  || ----- || ----- || ----- ||"
            print row3
            print "  ||_______||_______||_______||"

    def doMoves(self):
        currentPlayer='x'
        otherPlayer='y'
        tempPlayer=''
        self.printBoard()
        print "It is "+currentPlayer+"'s turn"
        x=int(raw_input('Enter starting x location '))
        y=int(raw_input('Enter starting y location '))
        currentBoard=(x, y)
        while self.board.winner=="N":
            self.printBoard()
            print "It is "+currentPlayer+"'s turn"
            print "You are playing in square ("+str(currentBoard[0])+", "+str(currentBoard[1])+")"
            entered=False
            while not entered:
                x=int(raw_input('Enter x location '))
                y=int(raw_input('Enter y location '))
                entered=self.board.move(currentPlayer, currentBoard[0], currentBoard[1], x, y)
                if entered==False:
                    print "That space is already taken, please try again"
            winner=self.board.checkWinner()
            while self.board.smallBoard.boardM[x][y]!='.':
                print "Board ("+str(x)+", "+str(y)+") has alreday been won"
                print "Player "+otherPlayer+" what square would you like to play in?"
                x=int(raw_input('Enter x location '))
                y=int(raw_input('Enter y location '))
            tempPlayer=currentPlayer
            currentPlayer=otherPlayer
            otherPlayer=tempPlayer
            tempPlayer=""
            currentBoard=(x, y)
        print "Congratulations player "+self.board.winner+" you have won the game!"
            

runner=Runner()
runner.doMoves()
            
        
