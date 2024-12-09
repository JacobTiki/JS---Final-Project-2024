# global gameBoard

gameBoard = [[" "," "," "], [" "," "," "], [" "," "," "]]
turn = int(0)

# Prints the tic tac toe board
def printBoard(board):
    # print the first line of dashes
    print("\n-------------")
    # iterate through each row
    for i in board:
        # print the first pipe 
        print("|", end="")
        # iterate through each column and print 
        for j in i:
            print(" %s |" %j, end="")
        # print line of dashes
        print("\n-------------")
    print()
def playGame():
    global gameBoard
    global turn
    # print(gameBoard)
    if(turn % 2 == 0):
        print("Player X's Turn:")
    else:
        print("Player O's Turn:")
    rowInput = int(input("Input the row to insert at, -1 to reset, -999 to quit:"))
    colInput = int(input("Input the column to insert at, -1 to reset, -999 to quit:"))
    if(rowInput == -999 or colInput == -999):
        exit()
    elif(rowInput == -1 or colInput == -1):
        gameBoard = [[" "," "," "], [" "," "," "], [" "," "," "]]
        print("Board Reset.")
        printBoard(gameBoard)
        playGame()
    elif(rowInput > 2 or colInput > 2):
        print("Invalid Input, Please Try Again.")
    else:
        if(gameBoard[rowInput][colInput] == "X" or gameBoard[rowInput][colInput] == "O"):
            print("Invalid Input, Please Try Again.")
        else:
            if(turn % 2 == 0):
                gameBoard[rowInput][colInput] = "X"
                printBoard(gameBoard)
            else:
                gameBoard[rowInput][colInput] = "O"
                printBoard(gameBoard)
    turn += 1
    # return gameBoard

while True:
    #print(playGame())
    playGame()