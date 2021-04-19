#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:20:13 2021

@author: caroline09
"""

import numpy as np



# Step 1 : Initialize an empty grid
class Connect4:
    
  def __init__(self):
    # nrows is the number of rows and ncols the number of columns
      self.nrows=6
      self.ncols=7
      self.board=np.zeros((self.nrows,self.ncols))


# Step 2 : Check if a column is full

  def IsColFull(self, NumCol):
    # NumCol is the column number
    ColElt =[]
    for row in self.board: 
      ColElt.append(row[NumCol])

    if 0 in ColElt:
       return False
    else:
       return True

# Step 3 : Insert a coin inside the board

  
  def InsertCoin(self,NumPl,NumCol):
    if self.IsColFull(NumCol)==False:
         for i in range(-1,-len(self.board[0]),-1) :
             if self.board[i][NumCol]==0:
                 self.board[i][NumCol]=NumPl
                 break
         print (self.board)
    else:
        NumCol = int(input('This column is full, please choose another column :'))
        return self.InsertCoin(NumPl)
        
        
# Step 4 : Check the board to see if there is a winning combination
## On the diagonals

  def CheckDiag(self):

    mat_diag1=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])    
    mat_diag2=np.array([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
    for i in range(6):
      for j in range(7):  
        c=self.board[i:4+i,j:4+j]
        if c.shape==(4,4):
          #print(c,i,j)
          compare_diag1_1 = (c*mat_diag1==mat_diag1)
          compare_diag1_2 = (c*mat_diag1==mat_diag1*2)
          compare_diag2_1 = (c*mat_diag2==mat_diag2)
          compare_diag2_2 = (c*mat_diag2==mat_diag2*2)

          # comparing the matrices with the diagonals
          if (compare_diag1_1.all() or compare_diag1_2.all())==True:
              if compare_diag1_1.all()==True:
                  print('Player 1 wins')
                  return True
              elif compare_diag1_2.all()==True:
                  print('Player 2 wins')
                  return True   

          if (compare_diag2_1.all() or compare_diag2_2.all())==True:
              if compare_diag2_1.all()==True:
                  print('Player 1 wins')
                  return True
              elif compare_diag2_2.all()==True:
                  print('Player 2 wins')
                  return True  


      
  ## On the rows

  def CheckRow(self):
      L1=[]
      L2=[]
      #print (d)
      for row in self.board:
          #print(row)
        for i in range(len(row)-3):
           # print(row[i:i+4],i)
              if set(row[i:i+4])==set([1,1,1,1]):
                  L1.append('True')
              if set(row[i:i+4])==set([2,2,2,2]):
                  L2.append('True')
   # print(L1)
   # print(L2)
      if 'True' in L1:
        print('Player 1 wins')
        return True                
      elif 'True' in L2:   
        print('Player 2 wins')
        return True               

## On the columns

  def CheckCol(self):
      L1=[]
      L2=[]
      d=np.transpose(self.board)
      #print (d)
      for row in d:
          #print(row)
          for i in range(len(row)-3):
             # print(row[i:i+4],i)
              if set(row[i:i+4])==set([1,1,1,1]):
                  L1.append('True')
              if set(row[i:i+4])==set([2,2,2,2]):
                  L2.append('True')
     # print(L1)
     # print(L2)
      if 'True' in L1:
          print('Player 1 wins')
          return True                
      elif 'True' in L2:   
          print('Player 2 wins')
          return True

# Step 5 : Display draw
  def IsBoardFull(self):
      if 0 not in self.board:
          print('The board is full')
  
# Step 6 : Play the game


class Player:
  def __init__(self,name,colour):
     self.name=name
     self.colour=colour
       
class Human(Player):
  def __init__(self,name,colour):
     Player.__init__(self,name,colour)

  def HChooseCol(self):
    NumCol = int(input('Player '+ self.name + ' please enter a number for column: '))
    return NumCol

class AI(Player):
  def __init__(self,name,colour):
     Player.__init__(self,name,colour)
     
  def AIChooseCol(self):
    NumCol = np.random.randint(7)
    m = ('Player '+ self.name + ' please enter a number for column: '+str(NumCol))
    print(m)
    return NumCol 
    
  
    
  
# Example of playing game (Human vs AI)       
c = Connect4()
h = Human('jojo','yellow')
a = AI('computer','red')

endgame=False
while endgame==False:
    # Player 1 Choosing a column
    c.InsertCoin(1,h.HChooseCol())
    if c.CheckDiag() or c.CheckRow() or c.CheckCol():   
        endgame=True
        break


  # Player 2 AI Choosing a column
    c.InsertCoin(2,a.AIChooseCol())
    if c.CheckDiag() or c.CheckRow() or c.CheckCol():   
        endgame=True
        break
    
    if c.IsBoardFull() and ((c.CheckDiag() or c.CheckRow() or c.CheckCol())==False):
        print('Nobody wins')
        endgame=True
        break