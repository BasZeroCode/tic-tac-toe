import random

board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

player = 'O'
computer = 'X'

def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

def spaceIsFree(position):
    return board[position] == ' '

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkWin():
            if letter == computer:
                print("Bot wins!")
            else:
                print("Player wins!")
            exit()
        if checkDraw():
            print("Draw!")
            exit()
    else:
        print("Invalid position")
        new_pos = int(input("Please enter a new position: "))
        insertLetter(letter, new_pos)

def checkWin():
    return (
        (board[1] == board[2] == board[3] != ' ') or
        (board[4] == board[5] == board[6] != ' ') or
        (board[7] == board[8] == board[9] != ' ') or
        (board[1] == board[4] == board[7] != ' ') or
        (board[2] == board[5] == board[8] != ' ') or
        (board[3] == board[6] == board[9] != ' ') or
        (board[1] == board[5] == board[9] != ' ') or
        (board[7] == board[5] == board[3] != ' ')
    )

def checkWhichMarkWon(mark):
    return (
        (board[1] == board[2] == board[3] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[7] == board[8] == board[9] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[3] == board[6] == board[9] == mark) or
        (board[1] == board[5] == board[9] == mark) or
        (board[7] == board[5] == board[3] == mark)
    )

def checkDraw():
    return all(board[key] != ' ' for key in board)

def playerMove():
    try:
        position = int(input("Enter a position for 'O' (1-9): "))
        if position not in board:
            print("Invalid input. Try again.")
            playerMove()
        else:
            insertLetter(player, position)
    except ValueError:
        print("Invalid input. Try again.")
        playerMove()

def compMove():
    bestScore = -800
    bestMove = 0
    for key in board:
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    insertLetter(computer, bestMove)

def minimax(board, isMaximizing):
    if checkWhichMarkWon(computer):
        return 1
    elif checkWhichMarkWon(player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -800
        for key in board:
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, False)
                board[key] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 800
        for key in board:
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '
                bestScore = min(score, bestScore)
        return bestScore

# Randomly decide who starts
print("Welcome to Tic-Tac-Toe!\n")
starter = random.choice(["player", "bot"])
printBoard(board)

if starter == "player":
    print("Player starts first!\n")
    while not checkWin():
        playerMove()
        compMove()
else:
    print("Bot starts first!\n")
    while not checkWin():
        compMove()
        playerMove()
