sudoku = [
    [0,0,0,0,7,0,0,0,0],
    [0,0,8,4,0,0,0,6,0],
    [0,3,0,2,9,0,0,5,0],

    [6,0,7,8,4,3,1,0,0],
    [0,8,0,5,2,9,0,4,0],
    [0,0,4,7,6,1,8,0,2],

    [0,1,0,0,8,4,0,7,0],
    [0,9,0,0,0,2,3,0,0],
    [0,0,0,0,5,0,0,0,0],
]

def solve(board):
    find = empty(board)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(board, i, (row, col)): # check the number
            board[row][col] = i # add the number
            if solve(board):
                return True
            board[row][col] = 0 # if not valid reset to 0
    return False

def print_board(board):
    for i in range(len(board)):
        if i%3==0 and i != 0:
            print('- - - - - - - - - - - ')
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print('| ', end='')
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')

def empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return(i, j)
    return None

def valid(board, num, pos):
    # rows
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # cols
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # box
    x = pos[1] // 3
    y = pos[0] // 3
    for i in range(y*3, y*3+3): # box position (e.g. 2*3=6 -> last box)
        for j in range(x*3, x*3+3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

print('\n- - - - - - - - ')
print('BOARD TO SOLVE:')
print('- - - - - - - - ')
print_board(sudoku)
print('\n- - - - - - - ')
solve(sudoku)
print('SOLVED BOARD:')
print('- - - - - - - ')
print_board(sudoku)