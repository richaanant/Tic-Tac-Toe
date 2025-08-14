import random
board = ["--", "--", "--", 
         "--","--", "--", 
         "--", "--", "--" ]

movingPlayer = "X"
winner = None
gameContinuing = True
# Printing the board
def printBoard(board):
    print(board[0] + "|" + board[1] +  "|" + board[2])
    print("--------")
    print(board[3] + "|" + board[4] +  "|" + board[5])
    print("--------")
    print(board[6] + "|" + board[7] +  "|" + board[8])
    print("--------")


# User input
def userInput(board):
    try:
        user = int(input("Enter the number from the board (1 - 9) : "))
        if user >= 1 and user <= 9:
            if board[user - 1] == "--":
                board[user - 1] = movingPlayer
                print("Spot has been placed") 
            else:
                print("Spot has been taken. Please choose an another spot")
        else:
            print("Invalid number, Please enter a number from 1 to 9")
    except ValueError:  
        print("Invalid value, cannot be converted to integer")


# Check Horizontal Match
def isRowMatch(board):
    global winner
    for i in range(0, 7, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != "--":
            winner = board[i]
            return winner
    return None

# Check Vertical Match
def isColMatch(board):
    global winner
    for i in range(0, 3, 1):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != "--":
           winner = board[i]
           return winner
    return None


# Check Diagonal Match
def isDiagMatch(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "--":
        winner = board[0]
        return winner
    elif board[2] == board[4] == board[6] and board[2] != "--":
        winner = board[2]
        return winner



# Change Players
def changePlayer():
    global movingPlayer
    if movingPlayer == "X":
        movingPlayer = "O"
    else:
        movingPlayer = "X"
  
# Check Tie
def checkTie(board):
    global gameContinuing
    if "--" not in board:
        printBoard(board)
        print("It is a tie")
        gameContinuing = False
    return gameContinuing


# Check Win
def checkWin(board):
   global gameContinuing
   if isRowMatch(board):
    printBoard(board)
    print("Game: Won: Winner is", winner)
    gameContinuing = False
    return gameContinuing
   
   elif isColMatch(board):
    printBoard(board)
    print("Game: Won: Winner is", winner)
    gameContinuing = False

   elif isDiagMatch(board):
    printBoard(board)
    print("Game: Won: Winner is", winner)
    gameContinuing = False
    return gameContinuing
    
       

# Computer Play
def computerBot(board):
    while movingPlayer == "O":  
        choice = random.randint(0, 8)
        if board[choice] == "--": 
            board[choice] = movingPlayer
            changePlayer()

# Loop running the game
while gameContinuing:
    printBoard(board)
    userInput(board)
    checkWin(board)
    checkTie(board)
    changePlayer()
    computerBot(board)
