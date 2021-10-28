global N
global gBoard
gBoard = [ [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0] ]
N = len(gBoard)

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = "\t")
        print()


def isSafeBad(board, row, col):
    for i in range(N):      # check for row
        if board[row][i] == 1:
            return False

    for i in range(N):      #check for column
        if board[i][col] == 1:
            return False

    c_row = row
    c_col = col

    while(c_row < N and c_col < N):     # check for down_right
        if(board[c_row][c_col] == 1):
            return False
        c_row += 1
        c_col += 1

    c_row = row
    c_col = col

    while(c_row < N and c_col >= 0):     # check for down_left
        if(board[c_row][c_col] == 1):
            return False
        c_row += 1
        c_col -= 1

    c_row = row
    c_col = col

    while(c_row >= 0 and c_col < N):     # check for up_right
        if(board[c_row][c_col] == 1):
            return False
        c_row -= 1
        c_col += 1

    while(c_row >= 0 and c_col >= 0):     # check for up_left
        if(board[c_row][c_col] == 1):
            return False
        c_row -= 1
        c_col -= 1
    return True
        
def isSafe(board, row, col): 
  
    # Check this row on left side 
    for i in range(col): 
        if board[row][i] == 1: 
            return False
  
    # Check upper diagonal on left side 
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    # Check lower diagonal on left side 
    for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    return True

def solveNQUtil(board, col):
    if col >= N:
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1

            if solveNQUtil(board, col+1) == True:
                return True

            board[i][col] = 0

    return False



def solveNQ():        
    if solveNQUtil(gBoard, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(gBoard)
    return True

solveNQ()
