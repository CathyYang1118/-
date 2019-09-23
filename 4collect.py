import numpy as np
import random

def ColumnNumberValid(board,row):
    valid = True
    if board[0][row-1] != '○':
        valid = False
    return valid

def ComputerMove(board,ID):
    global PrintInformation
    while 1:
        row = random.randint(1,7)
        if ColumnNumberValid(board,row) == True:
            for i in range(6):
                if board[5-i][row-1] == '○':
                    board[5-i][row-1] = '✠'
                    PrintIndformation = CheakIfThisPlayerHasWon(board,ID)
                    break
        break
    return board

def PlayerMove(board,ID):
    global PrintInformation
    run = True
    while run:
        row = int(input('Input a row to move:'))
        if row <= 7 and row >= 1 and ColumnNumberValid(board,row) == True:
            run = False
            for i in range(6):
                if board[5-i][row-1] == '○':
                    board[5-i][row-1] = '❖'
                    PrintIndformation = CheakIfThisPlayerHasWon(board,ID)
                    break
        else:
            print('Error')

    return board

def CheakHorizontal(board,WinCharacter):
    won = False
    for row in range(0,6):
        for i in range(0,4):
            if board[row][i] == WinCharacter and board[row][i+1] == WinCharacter and board[row][i+2] == WinCharacter and board[row][i+3] == WinCharacter:
                won = True
    return won

def CheakVertical(board,WinCharacter):
    won = False
    for row in range(0,3):
        for i in range(0,7):
            if board[row][i] == WinCharacter and board[row+1][i] == WinCharacter and board[row+2][i] == WinCharacter and board[row+3][i] == WinCharacter:
                won = True
    return won

def CheakSlantingRight(board,WinCharacter):
    won = False
    for row in range(0,3):
        for i in range(0,4):
            if board[row][i] == WinCharacter and board[row+1][i+1] == WinCharacter and board[row+2][i+2] == WinCharacter and board[row+3][i+3] == WinCharacter:
                won = True
    return won

def CheakSlantingLeft(board,WinCharacter):
    won = False
    for row in range(3,6):
        for i in range(0,4):
            if board[row][i] == WinCharacter and board[row-1][i+1] == WinCharacter and board[row-2][i+2] == WinCharacter and board[row-3][i+3] == WinCharacter :
                won = True
    return won

def CheakIfThisPlayerHasWon(board,ID):
    global WinnerFound
    character = '❖✠'
    WinCharacter = character [ID]
    print(WinCharacter)
    WinnerFound = False
    if CheakSlantingLeft(board,WinCharacter) == True or CheakSlantingRight(board,WinCharacter) == True or CheakHorizontal(board,WinCharacter) == True or CheakVertical(board,WinCharacter) == True:
        WinnerFound = True
    return WinnerFound

board=np.array([['○','○','○','○','○','○','○'],  
                ['○','○','○','○','○','○','○'],  
                ['○','○','○','○','○','○','○'],
                ['○','○','○','○','○','○','○'],
                ['○','○','○','○','○','○','○'],
                ['○','○','○','○','○','○','○']])

Total = 0
cheack = 1
WinnerFound = False

while 1:
    Total += 1
    cheack += 1
    PlareID = int(cheack % 2)
    print(PlayerMove(board,PlareID))
    print(' ___________________','\n','___________________','\n')
    if WinnerFound == True:
        print('player won')
        break
    cheack += 1
    ComputerID = int(cheack % 2)
    print(ComputerMove(board,ComputerID))
    print(' ___________________','\n','___________________','\n')
    if WinnerFound == True:
        print('computer won')
        break
    if Total == 14:
        print('game is finished')
        break
