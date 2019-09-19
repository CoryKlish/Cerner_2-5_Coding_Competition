theBoard = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8'}

def printBoard(board):
    print(board['0'] + ' | ' + board['1'] + ' | ' + board['2'])
    print('--+---+--')
    print(board['3'] + ' | ' + board['4'] + ' | ' + board['5'])
    print('--+---+--')
    print(board['6'] + ' | ' + board['7'] + ' | ' + board['8'])
    
def checkWin(boardList):
    # Rows
    for i in range(0, 9, 3):
        check = [boardList[i], boardList[i + 1], boardList[i + 2]]
        if all(val == 'O' for val in check) or all(val == 'X' for val in check): return True

    # Columns
    for i in range(0, 3, 1):
        check = [boardList[i], boardList[i + 3], boardList[i + 6]]
        if all(val == 'O' for val in check) or all(val == 'X' for val in check): return True

    # Diagonal
    diag1, diag2 = [boardList[0], boardList[4], boardList[8]], [boardList[2], boardList[4], boardList[6]]
    if all(val == 'O' for val in diag1) or all(val == 'X' for val in diag1): return True
    if all(val == 'O' for val in diag2) or all(val == 'X' for val in diag2): return True
    return False

turn = 'X'
for i in range(9):
    if checkWin(list(theBoard.values())):
        print('WINNER')
        break
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
