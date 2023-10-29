#Name: Aniket Nerkar
#Roll No. B_19
""" Python3 program to solve N Queen Problem
using Branch or Bound """
N = 8
""" A utility function to print solution """
def printSolution(board):
   for i in range(N):
    for j in range(N):
     print(board[i][j], end = " ")
    print()
    
    
""" A Optimized function to check if
a queen can be placed on board[row][col] """
def isSafe(row, col, slashCode, backslashCode,rowLookup, slashCodeLookup,backslashCodeLookup):
  if ( slashCodeLookup[slashCode[row][col]] or backslashCodeLookup[backslashCode[row][col]] or rowLookup[row]) :
      return False
  return True


""" A recursive utility function
 to solve N Queen problem """
 
def solveNQueensUtil(board, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
 
 """ base case: If all queens are
 placed then return True """
 if(col >= N):
    return True
 for i in range(N):
  if(isSafe(i, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup)):
     board[i][col] = 1
     rowLookup[i] = True
     slashCodeLookup[slashCode[i][col]] = True
     backslashCodeLookup[backslashCode[i][col]] = True
     """ recur to place rest of the queens """
     if(solveNQueensUtil(board, col + 1,slashCode, backslashCode,rowLookup, slashCodeLookup, backslashCodeLookup)):
         return True
     board[i][col] = 0
     rowLookup[i] = False
     slashCodeLookup[slashCode[i][col]] = False
     backslashCodeLookup[backslashCode[i][col]] = False
 return False

def solveNQueens():
     board = [[0 for i in range(N)]for j in range(N)]
     slashCode = [[0 for i in range(N)]for j in range(N)]
     backslashCode = [[0 for i in range(N)]for j in range(N)]
     rowLookup = [False] * N
     x = 2 * N - 1
     slashCodeLookup = [False] * x
     backslashCodeLookup = [False] * x
     for rr in range(N):
       for cc in range(N):
        slashCode[rr][cc] = rr + cc
        backslashCode[rr][cc] = rr - cc + 7
 
     if(solveNQueensUtil(board, 0, slashCode, backslashCode,rowLookup, slashCodeLookup, backslashCodeLookup) == False):
      print("Solution does not exist")
      return False
 
     printSolution(board)
     return True
 
solveNQueens()

 
