class Board:
    'A class for inner boards'

    def __init__(self):
        temp=[]
        for i in range(3):
            temp.append([])
            for j in range(3):
                temp[i].append('.')
        self.boardM=temp
        self.winner="N"

    def move(self, player, x, y):
        if self.boardM[x][y]=='.':
            self.boardM[x][y]=player
            return True
        else:
            return False

    def checkWinner(self):
        if self.winner != "N":
            return self.winner
        for i in range(3):
            tempPlayer=self.boardM[i][0]
            if tempPlayer!='.':
                if tempPlayer==self.boardM[i][1] and tempPlayer==self.boardM[i][2]:
                    self.winner=tempPlayer
                    return self.winner
            tempPlayer=self.boardM[0][i]
            if tempPlayer!='.':
                if tempPlayer==self.boardM[1][i] and tempPlayer==self.boardM[2][i]:
                    self.winner=tempPlayer
                    return self.winner
        tempPlayer=self.boardM[0][0]
        if tempPlayer!='.':
            if tempPlayer==self.boardM[1][1] and tempPlayer==self.boardM[2][2]:
                self.winner=tempPlayer
                return self.winner
        tempPlayer=self.boardM[0][2]
        if tempPlayer!='.':
            if tempPlayer==self.boardM[1][1] and tempPlayer==self.boardM[2][0]:
                self.winner=tempPlayer
                return self.winner
        return '.'
            
