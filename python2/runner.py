from board import Board

class tttRunner:
    'Runner for Tic Tac Toe game'
    
    def __init__(self):
        self.board=Board()

        
    def printBoard(self):
        arr=self.board.boardM
        print "-------"
        for i in xrange(3):
            row="|"
            for j in xrange(3):
                row=row+arr[i][j]+"|"
            print row
            print "-------"

    def doMoves(self):
        currentPlayer='x'
        otherPlayer='y'
        tempPlayer=''
        while self.board.winner=="N":
            print self.board.winner
            self.printBoard()
            print "It is "+currentPlayer+"'s turn"
            entered=False
            while not entered:
                x=int(raw_input('Enter x location '))
                y=int(raw_input('Enter y location '))
                entered=self.board.move(currentPlayer, x, y)
                if entered==False:
                    print "That space is already taken, please try again"
            winner=self.board.checkWinner()
            tempPlayer=currentPlayer
            currentPlayer=otherPlayer
            otherPlayer=tempPlayer
            tempPlayer=""
            

runner=tttRunner()
runner.doMoves()
            
        
