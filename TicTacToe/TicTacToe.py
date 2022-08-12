board = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-']]  

def display_board():
    print(board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('--+---+--')
    print(board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('--+---+--')
    print(board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])
    
def play():
    turn = 'X'
    winner = ''
    while not winner:
        valid_move=False
        display_board()
        print('\nIt\'s your turn,', turn,'move to which place?')
        while not valid_move:
            row = int(input('Select the row (0, 1, 2): '))
            col = int(input('Now select the column (0, 1, 2): '))
            if col < 0 or row < 0 or col > 2 or row > 2:
                print('You have to insert numbers between 0-2')
                continue
            if board[row][col] != '-':
                print('\nThis place is already filled.\nMove to which place?')
                continue
            valid_move=True
            board[row][col] = turn
            winner = check_winner()
        if turn == 'X':
          turn = 'O'
        else:
          turn = 'X'
    print('\n' + winner, "won")  
    
def check_winner():
    #rows
      if board[0][0] == board[0][1] == board[0][2] and board[0][0] != '-':
        return board[0][0] # 
      elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != '-':
        return board[1][0]
      elif board[2][0] == board[2][1] == board[0][2] and board[2][0] != '-':
        return board[2][0]
      #cols
      elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != '-':
        return board[0][0]
      elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != '-':
        return board[0][1]
      elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != '-':
        return board[0][2]
      #diagonals
      elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return board[0][0]
      elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return board[0][2]

      #check if the board is full
      for r in [0, 1, 2]:
        for c in [0, 1, 2]:
          if board[r][c] == '-': # there's at least one space still available
            return ''

      return 'Nobody'

play()