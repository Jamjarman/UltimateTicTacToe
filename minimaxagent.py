class MinimaxAgent:

    def __init__(self, off, deff, player, depth):
        self.No=off
        self.Nd=deff
        self.player=player
        self.depth=depth
        

    def simulateMoves(self, board, currBoard):
        moves=[]
        for i in xrange(3):
            for j in xrange(3):
                if board.largeBoard[currBoard[0]][currBoard[1]].boardM[i][j]=='.':
                    moves.append((i, j))
    
    def score(self, board):
        temp=[]
        for i in xrange(3):
            temp.append([])
            for j in xrange(3):
                temp[i].append(self.scoreSmall(board.largeBoard[i][j]))
        
                
    def scoreSmall(self, board):
        arr=board.boardM
        if board.checkWinner()==self.player:
            return (1, 0)
        else if board.checkWinner()!=self.player and board.checkWinner()!='.':
            return (0, 1)
        rowsumP=0
        colsumP=0
        disumP=0
        rowsumO=0
        colsumO=0
        disumO=0
        defP=0
        defO=0
        #todo, include analysis of diagonals
        numArr=self.makeNum(arr)
        for i in xrange(3):
            trowsumP=0
            tcolsumP=0
            trowsumO=0
            tcolsumO=0
            rowSum=0
            colSum=0
            for j in xrange(3):
                rowSum+=numArr[i][j]
                colSum+=numArr[i][j]
                if numArr[i][j]>0:
                    trowsumP+=numArr[i][j]
                    tcolsumP+=numArr[j][i]
                else if numArr[i][j]<0:
                    trowsumO+=numArr[i][j]
                    tcolsumO+=numArr[j][i]
            rowsumP+=trowsumP/3
            colsumP+=tcolsumP/3
            rowsumO+=trowsumO/-3
            colsumO+=tcolsumO/-3
            #This is a hacked method, it shouldn't allow for a row or column where only the opponent has one but this works for now
            if rowSum==-1:
                defP+=1
            else if rowSum==1:
                defO+=1
            if colSum==-1:
                defP+=1
            else if colSum==1:
                defO+=1
        attScoreP=self.No*(colsumP+rowsumP)/8
        attScoreO=self.No*(colsumO+rowsumO)/8
        defScoreP=self.Nd*(defP/4)
        defScoreO=self.Nd*(defO/4)
        scoreP=attScoreP+defScoreP
        scoreO=attScoreO+defScoreO
        finScoreO=scoreO/(scoreO+scoreP)
        finScoreP=scoreP/(scoreO+scoreP)
        return (finScoreP, finScoreO)
        
        
                
                
    def makeNum(self, arr):
        temp=[]
        for i in xrange(3):
            for j in xrange(3):
                if arr[i][j]==self.player:
                    temp[i].append(1)
                else if arr[i][j]!='.':
                    temp[i].append(-1)
                else:
                    temp[i].append(0)
        return temp
    

    def analyze(self, board, currBoard, currDepth, player, otherPlayer):
        if currDepth<self.depth:
            if board.smallBoard.boardM[currBoard[0]][currBoard[1]]=='.':
                moveList=self.simulateMoves(board, currBoard)
            else:
                for i in xrange(3):
                    for j in xrange(3):
                        moveList[]
                        if board.smallBoard.boardM[i][j]=='.':
                            moveList=moveList+simulateMoves(board, (i, j))
            scoreList=[]
            for move in moveList:
                modBoard=board.move(player, currBoard[0], currBoard[1], move[0], move[1])
                scoreList.append(self.analyze(modBoard, move, currDepth+1, otherPlayer, player)
            bestI=-1
            minVal=100000000
            maxVal=-1
            for i in xrange(len(scoreList)):
                if scoreList[i][0]>maxVal:
                    bestI=i
                    maxVal=scoreList[i][0]
                    minVal=scoreList[i][1]
                else if scoreList[i][0]==maxVal and scoreList[i][1]<minVal:
                    bestI=i
                    maxVal=scoreList[i][0]
                    minVal=scoreList[i][1]
            if currDepth==1:
                return moveList[i]
            else:
                return scoreList[i]
        else:
            scoreTuple=self.score(board)
            return scoreTuple
            
