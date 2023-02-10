columns = 7
rows = 6

board = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]


def printBoard():
    for row in range(0, rows):
        for col in range(0, columns):
            print(board[row][col], end=' ')
        print(" ")


def fill(col, player):
    col = col-1
    for row in range(rows-1, -1, -1):
        if board[row][col] == 0:
            print("legal move")
            board[row][col] = player
            break


usernum = int(input("Select 1-7:"))
fill(usernum, 1)
printBoard()


usernumtwo = int(input("Select 1-7:"))
fill(usernumtwo, 2)
printBoard()
