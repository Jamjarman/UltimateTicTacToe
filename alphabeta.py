from __future__ import division
import copy
import pdb
from board import Board
from ultimateBoard import UltimateBoard


class AlphaBetaAgent:

    #Initialize agent with offensive and defensive modifiers, depth, and which player it is acting as
    def __init__(self, off, deff, player, opponent, depth):
        self.No=off
        self.Nd=deff
        self.player=player
        self.depth=depth
        self.opp=opponent
        
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
            return -121
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
            return -12
        arr=board.boardM
        numArr=self.makeNum(arr, player)
        rowpoints=0
        colpoints=0
        defpoints=0
        tempRow=0
        tempCol=0
        tempRowO=0
        tempColO=0
        rowScore=0
        colScore=0
        rowScoreO=0
        colScoreO=0
        rowAbs=0
        colAbs=0
        diaPoints=0
        lrDiagonalAbs=0
        rlDiagonalAbs=0
        lrDiagonalAct=0
        rlDiagonalAct=0
        for i in xrange(3):
            for j in xrange(3):
                if numArr[i][j]>0:
                    tempRow+=1
                elif numArr[i][j]<0:
                    tempRowO-=1
                if numArr[j][i]>0:
                    tempCol+=1
                elif numArr[j][i]<0:
                    tempColO-=1
                rowAbs+=abs(numArr[i][j])
                colAbs+=abs(numArr[j][i])
                rowScore+=numArr[i][j]
                colScore+=numArr[j][i]
            if numArr[i][i]>0:
                diaPoints+=1
            lrDiagonalAbs+=abs(numArr[i][i])
            lrDiagonalAct+=numArr[i][i]
            if i==0:
                if numArr[0][2]>0:
                    diaPoints+=1
                rlDiagonalAbs+=abs(numArr[0][2])
                rlDiagonalAct+=numArr[0][2]
            elif i==1:
                if numArr[1][1]>0:
                    diaPoints+=1
                rlDiagonalAbs+=abs(numArr[1][1])
                rlDiagonalAct+=numArr[1][1]
            elif i==2: 
                if numArr[2][0]>0:
                    diaPoints+=1
                rlDiagonalAbs+=abs(numArr[2][0])
                rlDiagonalAct+=numArr[2][0]
            rowpoints+=tempRow/3
            #rowpoints-=tempRowO/3
            colpoints+=tempCol/3
            #colpoints-=tempColO/3
            if rowAbs==3 and rowScore==-1:
                defpoints+=1
            #elif rowAbs==3 and rowScore==1:
                #defpoints-=1
            if colAbs==3 and colScore==-1:
                defpoints+=1
            #elif colAbs==3 and colScore==1:
                #defpoints-=1
        if rlDiagonalAbs==3 and rlDiagonalAct==-1:
            defpoints+=1
        if lrDiagonalAbs==3 and lrDiagonalAct==-1:
            defpoints+=1
        score=(rowpoints+colpoints+diaPoints/6)*self.No+defpoints*self.Nd
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
    

    def analyze(self, board, currentBoard, depth, alpha, beta):
        if depth<self.depth:
            bestMove=(1, 1)
            moves=[]
            score=0
            modDepth=0
            player=""
            if depth%1==0:
                score=-999999
                player=self.player
            elif depth%1==.5:
                score=999999
                player=self.opp
            if board.smallBoard.boardM[currentBoard[0]][currentBoard[1]]=='.':
                moves=self.simulateMoves(board, currentBoard)
                modDepth=depth+.5
            else:
                for i in xrange(3):
                    for j in xrange(3):
                        if board.smallBoard.boardM[i][j]=='.':
                            moves.append((i, j))
                modDepth=depth
            #iterate through moves
            for move in moves:
                #call analyze on moved board, with alpha and beta switched if needed
                boardCopy=copy.deepcopy(board)
                if depth!=modDepth:
                    boardCopy.move(player, currentBoard[0], currentBoard[1], move[0], move[1])
                if depth%1==0:
                    alphaSend=score
                    betaSend=beta
                elif depth%1==.5:
                    alphaSend=alpha
                    betaSend=score
                tempScore=self.analyze(boardCopy, move, modDepth, alphaSend, betaSend)
                #if score is better than v score replaces v
                #check v against alpha or beta
                #if check is positive return v
                #if depth=0 return move of best v
                if depth%1==0:
                    if tempScore>score:
                        score=tempScore
                        bestMove=move
                    if score>beta:
                        if depth>0:
                            return score
                        else:
                            return move
                elif depth%1==.5:
                    if tempScore<score:
                        score=tempScore
                        bestMove=move
                    if score<alpha:
                        if depth>0:
                            return score
                        else:
                            return move
            if depth==0:
                return bestMove
            else:
                return score
        else:
            return self.score(board, self.player, self.opp)



        
