the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print()


def checkWin(board):
    if board['top-L'] is board['top-M'] is board['top-R']:
        return board['top-L']
    if board['mid-L'] is board['mid-M'] and board['mid-L'] is board['mid-R']:
        return board['mid-L']
    if board['bot-L'] is board['bot-M'] and board['bot-L'] is board['bot-R']:
        return board['bot-L']

turn = 'X'
for i in range(9):
    printBoard(the_board)
    
    print(f'Turn for {turn}. Move on which space?')
    move = input()
    the_board[move] = turn
    if turn is 'X':
        turn = 'O'
    else:
        turn = 'X'
    checkWin(the_board)
printBoard(the_board)

    