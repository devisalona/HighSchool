import os
import sys
class TicTacToe(object):
    def __init__(self):
        self.data = list([0,0,0,0,0,0,0,0,0])
        self.player = ['X',' ','O']
        self.Print()
    def Print(self):
        print "Human = X, Computer = O"
        for j in range(3):
            print '%1c | %1c | %1c' % (self.player[self.data[3*j]+1],self.player[self.data[3*j+1]+1],self.player[self.data[3*j+2]+1]), "\n---------"
    def gameOver(self):
        #print self.data
        if self.winnerIs() == 0:
            return False
        return True
    def move(self, i, s):
	if self.data[i] == 0:
        	self.data[i] = s
		self.Print()
	else:
		self.Print()
		print "INVALID MOVE"
		m = int(input("Make your move: "))
		self.move(m-1,-1)

    def winnerIs(self):
        winner = 0
        for t in range(3):
            if (self.data[3*t] == self.data[3*t+1] == self.data[3*t+2]) and self.data[3*t] != 0: 
                winner = self.data[3*t]
                break
            if (self.data[t] == self.data[t+3] == self.data[t+6]) and self.data[t] != 0:
                winner = self.data[t]
                break
        if winner == 0 and (self.data[0] == self.data[4] == self.data[8]) and self.data[0] != 0:
            winner =  self.data[0]
        if winner == 0 and (self.data[2] == self.data[4] == self.data[6]) and self.data[2] != 0:
            winner = self.data[2]
        return winner
    def istrap(self,board,player):
        nwins = 0
        for i in range(len(board)):
            if(board[i] == 0): 
                board[i] = player
                if(self.winnerIs() == player):
                    nwins += 1
                board[i] = 0
        if nwins > 1:
            return 1
        else:
            return 0
    def computerMove(self):
        position = 0
        # first try an immediate win 
        #print 'in check loop'
        for i in range(len(self.data)):
            if(self.data[i] == 0 ): 
                self.data[i] = 1
                #print 'checking position ', i
                if self.winnerIs() == 1:
                    position = i
                    #print 'immediate win', position + 1
                    self.data[i] = 0
                    break
                self.data[i] = 0
            #print self.data
            position == 0
            #block the opponent if they can win
            #print 'in opponent check loop'
            for i in range(len(self.data)):
                if(self.data[i] == 0 ): 
                    self.data[i] = -1
                    #print 'checking position ', i, self.winnerIs()
                    if self.winnerIs() == -1:
                        position = i
                        #print 'opponent win', position + 1
                        self.data[i] = 0
                        break
                    self.data[i] = 0
        #evaluate probability of winning with different moves
        if position == 0:
            prob = [-1000000,-1000000,-1000000,-1000000,-1000000,-1000000,-1000000,-1000000,-1000000]
            self.evaluate(self.data,prob,1,0)
            #print prob
            position = prob.index(max(prob))
        # Make the selected move
        self.move(position,1)
        
    def evaluate(self,board,prob,player, level):
        if(self.winnerIs() == 1):
            return 1
        if(self.winnerIs() == -1):
            return -2
        count = 0
        for i in board:
            if i == 1 or i == -1:
                count += 1
        if(self.winnerIs() == 0 and count == 9):
            return 0
        result = 0
        for i in range(len(board)):
            if(board[i] == 0): 
                board[i] = player
                if self.istrap(board,player):
                    #print 'trap position=',i+1, ' player=',player,' level=', level
                    temp= 9
                else:
                    level += 1
                    temp = self.evaluate(board,prob, -1*player, level)
                    level -= 1
                if (level != 0):
                    result += temp
                else:
                    #print 'position=',i+1, ' player=',player,' level=', level,'result=',temp
                    result = temp
                    prob[i] = result
                board[i] = 0
        return result
            
            

def clearScreen():
    print ("\n " * 50)

sys.setrecursionlimit(500000)
A = TicTacToe()
i = 0
while (A.gameOver() == False and i < 9):
    m = int(input("Make your move: "))
    clearScreen()
    i += 1
    A.move(m-1, -1)
    r = A.gameOver()
    #print r
    if(A.gameOver() == False and i < 9):
        i +=1
        A.computerMove()
if A.winnerIs() == 1:
    print "Computer is the winner."
elif A.winnerIs() == -1:
    print "You are the winner."
else:
    print "The game is a tie."


