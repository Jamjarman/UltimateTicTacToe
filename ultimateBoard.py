from board import Board

class UltimateBoard:
    'A class for inner boards'

    def __init__(self):
        temp=[]
        for i in xrange(3):
            temp.append([])
            for j in xrange(3):
                temp[i].append(Board())
        self.largeBoard=temp
        self.smallBoard=Board()
        self.winner="N"

    def move(self, player, largeX, largeY, smallX, smallY):
        if self.largeBoard[largeX][largeY].boardM[smallX][smallY]=='.':
            self.largeBoard[largeX][largeY].boardM[smallX][smallY]=player
            return True
        else:
            return False


    def checkBoards(self):
        for i in xrange(3):
            for j in xrange(3):
                localWinner=self.largeBoard[i][j].checkWinner()
                self.smallBoard.boardM[i][j]=localWinner

    def checkWinner(self):
        self.checkBoards()
        if self.winner != "N":
            return self.winner
        for i in xrange(3):
            tempPlayer=self.smallBoard.boardM[i][0]
            if tempPlayer!='.':
                if tempPlayer==self.smallBoard.boardM[i][1] and tempPlayer==self.smallBoard.boardM[i][2]:
                    self.winner=tempPlayer
                    return self.winner
            tempPlayer=self.smallBoard.boardM[0][i]
            if tempPlayer!='.':
                if tempPlayer==self.smallBoard.boardM[1][i] and tempPlayer==self.smallBoard.boardM[2][i]:
                    self.winner=tempPlayer
                    return self.winner
        tempPlayer=self.smallBoard.boardM[0][0]
        if tempPlayer!='.':
            if tempPlayer==self.smallBoard.boardM[1][1] and tempPlayer==self.smallBoard.boardM[2][2]:
                self.winner=tempPlayer
                return self.winner
        tempPlayer=self.smallBoard.boardM[0][2]
        if tempPlayer!='.':
            if tempPlayer==self.smallBoard.boardM[1][1] and tempPlayer==self.smallBoard.boardM[2][0]:
                self.winner=tempPlayer
                return self.winner
                
            
