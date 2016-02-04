from __future__ import division
import copy
import pdb
from board import Board
from ultimateBoard import UltimateBoard


class MinimaxAgent:

    #Initialize agent with offensive and defensive modifiers, depth, and which player it is acting as
    def __init__(self, off, deff, player, opponent, depth):
        self.No=off
        self.Nd=deff
        self.player=player
        self.depth=depth
        self.opp=opponent
        self.pruneList=[]
        
    #get list of all possible legal moves in the give square, return as list of tuples
    def simulateMoves(self, board, currBoard):
        moves=[]
        for i in xrange(3):
            for j in xrange(3):
                if board.largeBoard[currBoard[0]][currBoard[1]].boardM[i][j]=='.':
                    moves.append((i, j))
        return moves

    #get a score for the board, add score for large board to scores for small boards
    def score(self, board, player, opponent):
        if board.smallBoard.checkWinner()==player:
            return 121
        elif board.smallBoard.checkWinner()==opponent:
            return 0
        score=0
        score+=self.scoreSquare(board.smallBoard, player, opponent)
        for i in xrange(3):
            for j in xrange(3):
                score+=self.scoreSquare(board.largeBoard[i][j], player, opponent)
        return score
    
    #Currently implemented to ignore opponent's pieces except for defense calc and to check if opponent has won square
    def scoreSquare(self, board, player, opponent):
        if board.checkWinner()==player:
            return 12
        elif board.checkWinner()==opponent:
            return 0
        arr=board.boardM
        numArr=self.makeNum(arr, player)
        rowpoints=0
        colpoints=0
        defpoints=0
        tempRow=0
        tempCol=0
        rowScore=0
        colScore=0
        rowAbs=0
        colAbs=0
        for i in xrange(3):
            for j in xrange(3):
                if numArr[i][j]>0:
                    tempRow+=1
                if numArr[j][i]>0:
                    tempCol+=1
                rowAbs+=abs(numArr[i][j])
                colAbs+=abs(numArr[j][i])
                rowScore+=numArr[i][j]
                colScore+=numArr[j][i]
            rowpoints+=tempRow/3
            colpoints+=tempCol/3
            if rowAbs==3 and rowScore==-1:
                defpoints+=1
            if colAbs==3 and colScore==-1:
                defpoints+=1
        score=rowpoints+colpoints+defpoints
        return score
                        
                
    def makeNum(self, arr, plyr):
        temp=[]
        for i in xrange(3):
            temp.append([])
            for j in xrange(3):
                if arr[i][j]==plyr:
                    temp[i].append(1)
                elif arr[i][j]!='.':
                    temp[i].append(-1)
                else:
                    temp[i].append(0)
        return temp
    

    def analyze(self, board, currBoard, currDepth, player, otherPlayer):
        moveList=[]
        scoreList=[]
        if currDepth<self.depth:
            temp1=currBoard[0]
            temp2=currBoard[1]
            if board.smallBoard.boardM[temp1][temp2]=='.':
                #print "Board is open checking moves"
                moveList=self.simulateMoves(board, currBoard)
                #print moveList
                for move in moveList:
                    copyBoard=copy.deepcopy(board)
                    copyBoard.move(player, currBoard[0], currBoard[1], move[0], move[1])
                    scoreList.append(self.analyze(copyBoard, move, currDepth+1, otherPlayer, player))
            else:
                #print "Board is closed check other boards"
                for i in xrange(3):
                    for j in xrange(3):
                        if board.smallBoard.boardM[i][j]=='.':
                            moveList.append((i, j))
                for move in moveList:
                    scoreList.append(self.analyze(board, move, currDepth, player, otherPlayer))
            bestI=-1
            bestVal=-1
            for i in xrange(len(scoreList)):
                if player==self.player:
                    if scoreList[i][0]>bestVal:
                        bestI=i
                        bestVal=scoreList[i][0]
                elif player==self.opp:
                    if scoreList[i][1]<bestVal:
                        bestI=i
                        bestVal=scoreList[i][1]
            if currDepth==1:
                return moveList[bestI]
            else:
                return scoreList[bestI]
        else:
            scoreTuple=(self.score(board, self.player, self.opp), self.score(board, self.opp, self.player))
            return scoreTuple
            
