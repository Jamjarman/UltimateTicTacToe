from __future__ import division
import copy
import pdb
from board import Board
from ultimateBoard import UltimateBoard


class MinimaxAgent:

    #Initialize agent with offensive and defensive modifiers, depth, and which player it is acting as
    def __init__(self, off, deff, player, depth):
        self.No=off
        self.Nd=deff
        self.player=player
        self.depth=depth
        self.output=open('output.txt', 'w')
        
    #get list of all possible legal moves in the give square, return as list of tuples
    def simulateMoves(self, board, currBoard):
        moves=[]
        for i in xrange(3):
            for j in xrange(3):
                if board.largeBoard[currBoard[0]][currBoard[1]].boardM[i][j]=='.':
                    moves.append((i, j))
        return moves

    #get a score for the board
    def score(self, board):
        self.output.write("Getting score for board \n")
        #pdb.set_trace()
        temp=[]
        #create a 3x3 array of scores of each of the small grids, each grid box contains a tuple of 
        #(player score, opponent score)
        for i in xrange(3):
            temp.append([])
            for j in xrange(3):
                #call scoreSmall to score the individual board and append it to the array
                temp[i].append(self.scoreSmall(board.largeBoard[i][j]))
        self.output.write("Score table: "+str(temp)+"\n")
        #print temp
        playerScore=0
        opponentsScore=0
        #iterate through array and calculate overall score for array
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
        self.output.write("Player score: "+str(playerScore)+" Opponent Score: "+str(opponentsScore)+"\n")
        if board.checkWinner()==self.player:
            self.output.write("Player will win\n")
            playerScore=playerScore*3
            opponentsScore=opponentsScore/3
        elif board.checkWinner()!=self.player and board.checkWinner()!='.' and board.checkWinner()!='N':
            self.output.write("Opponent will win"+board.checkWinner()+"\n")
            playerScore=playerScore/3
            opponentsScore=opponentsScore*3
        return (playerScore, opponentsScore) 
                
                
    def scoreSmall(self, board):
        arr=board.boardM
        if board.checkWinner()==self.player:
            return (1, 0)
        elif board.checkWinner()!=self.player and board.checkWinner()!='.':
            return (0, 1)
        self.output.write("Evaluating mini board: "+str(arr)+"\n")
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
            rowSumAct=0
            colSumAct=0
            for j in xrange(3):
                rowSum+=numArr[i][j]
                colSum+=numArr[j][i]
                rowSumAct+=abs(numArr[i][j])
                colSumAct+=abs(numArr[j][i])
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
            if rowSum==-1 and rowSumAct==3:
                defP+=1
            elif rowSum==1 and rowSumAct==3:
                defO+=1
            if colSum==-1 and colSumAct==3:
                defP+=1
            elif colSum==1 and colSumAct==3:
                defO+=1
        attScoreP=self.No*(colsumP+rowsumP)/8
        attScoreO=self.No*(colsumO+rowsumO)/8
        defScoreP=self.Nd*(defP/4)
        defScoreO=self.Nd*(defO/4)
        scoreP=attScoreP+defScoreP
        scoreO=attScoreO+defScoreO
        self.output.write("Final score for board"+str((scoreP, scoreO))+"\n")
        return (scoreP, scoreO)
        
        
                
                
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
        scoreList=[]
        self.output.write("Entering Analyze, depth: "+str(currDepth)+" player: "+player+" currBoard"+str(currBoard)+"\n")
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
            bestVal=0
            self.output.write("Evaluating score list: "+str(scoreList)+"\n")
            if player==self.player:
                bestVal=-1
            else:
                bestVal=999999999                
            for i in xrange(len(scoreList)):
                if player==self.player:
                    if scoreList[i][0]>bestVal:
                        bestI=i
                        bestVal=scoreList[i][0]
                else:
                    if scoreList[i][1]<bestVal:
                        bestI=i
                        bestVal=scoreList[i][1]
            if currDepth==1:
                self.output.write("Returning move "+str(moveList[bestI])+"\n")
                return moveList[bestI]
            else:
                self.output.write("Returning scorelist "+str(scoreList[bestI])+"\n")
                return scoreList[bestI]
        else:
            scoreTuple=self.score(board)
            self.output.write("Returning score tuple from lowest level "+str(scoreTuple)+"\n")
            return scoreTuple
            
