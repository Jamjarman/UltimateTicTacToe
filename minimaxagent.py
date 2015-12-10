from __future__ import division
import copy
import pdb
from board import Board
from ultimateBoard import UltimateBoard


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
        return moves
    
    def score(self, board):
        #pdb.set_trace()
        temp=[]
        for i in xrange(3):
            temp.append([])
            for j in xrange(3):
                temp[i].append(self.scoreSmall(board.largeBoard[i][j]))
        #print temp
        playerScore=0
        opponentsScore=0
        for i in xrange(3):
            playerScoreTR=0
            playerScoreCR=0
            oppScoreTR=0
            oppScoreCR=0
            for j in xrange(3):
                playerScoreTR+=temp[i][j][0]
                playerScoreCR+=temp[j][i][0]
                oppScoreTR+=temp[i][j][1]
                oppScoreCR+=temp[j][i][1]
            playerScore+=playerScoreTR/3+playerScoreCR/3
            opponentsScore+=oppScoreTR/3+oppScoreCR/3
        return (playerScore, opponentsScore) 
                
                
    def scoreSmall(self, board):
        arr=board.boardM
        if board.checkWinner()==self.player:
            return (1, 0)
        elif board.checkWinner()!=self.player and board.checkWinner()!='.':
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
                colSum+=numArr[j][i]
                if numArr[i][j]>0:
                    trowsumP+=numArr[i][j]
                elif numArr[i][j]<0:
                    trowsumO+=numArr[i][j]
                if numArr[j][i]>0:
                    tcolsumP+=numArr[j][i]
                elif numArr[j][i]<0:
                    tcolsumO+=numArr[j][i]
            rowsumP+=trowsumP/3
            colsumP+=tcolsumP/3
            rowsumO+=trowsumO/-3
            colsumO+=tcolsumO/-3
            #This is a hacked method, it shouldn't allow for a row or column where only the opponent has one but this works for now
            if rowSum==-1:
                defP+=1
                #print "def"+str(defP)
            elif rowSum==1:
                defO+=1
                #print "def"+str(defO)
            if colSum==-1:
                defP+=1
                #print "def"+str(defP)
            elif colSum==1:
                defO+=1
                #print "Def"+str(defP)
        attScoreP=self.No*(colsumP+rowsumP)/8
        attScoreO=self.No*(colsumO+rowsumO)/8
        defScoreP=self.Nd*(defP/4)
        defScoreO=self.Nd*(defO/4)
        scoreP=attScoreP+defScoreP
        scoreO=attScoreO+defScoreO
        if scoreO+scoreP>0:
            finScoreO=scoreO/(scoreO+scoreP)
            finScoreP=scoreP/(scoreO+scoreP)
        else:
            finScoreO=0
            finScoreP=0
        return (finScoreP, finScoreO)
        
        
                
                
    def makeNum(self, arr):
        temp=[]
        for i in xrange(3):
            temp.append([])
            for j in xrange(3):
                if arr[i][j]==self.player:
                    temp[i].append(1)
                elif arr[i][j]!='.':
                    temp[i].append(-1)
                else:
                    temp[i].append(0)
        return temp
    

    def analyze(self, board, currBoard, currDepth, player, otherPlayer):
        moveList=[]
        if currDepth<self.depth:
            temp1=currBoard[0]
            temp2=currBoard[1]
            if board.smallBoard.boardM[temp1][temp2]=='.':
                #print "Board is open checking moves"
                moveList=self.simulateMoves(board, currBoard)
            else:
                #print "Board is closed check other boards"
                for i in xrange(3):
                    for j in xrange(3):
                        if board.smallBoard.boardM[i][j]=='.':
                            moveList=moveList+self.simulateMoves(board, (i, j))
            scoreList=[]
            #print moveList
            for move in moveList:
                copyBoard=copy.deepcopy(board)
                copyBoard.move(player, currBoard[0], currBoard[1], move[0], move[1])
                scoreList.append(self.analyze(copyBoard, move, currDepth+1, otherPlayer, player))
            best=-1
            minVal=100000000
            maxVal=-1
            #print scoreList
            for i in xrange(len(scoreList)):
                if scoreList[i][0]>maxVal:
                    best=i
                    maxVal=scoreList[i][0]
                    minVal=scoreList[i][1]
                elif scoreList[i][0]==maxVal and scoreList[i][1]<minVal:
                    best=i
                    maxVal=scoreList[i][0]
                    minVal=scoreList[i][1]
            if currDepth==1:
                return moveList[best]
            else:
                return scoreList[best]
        else:
            scoreTuple=self.score(board)
            return scoreTuple
            
