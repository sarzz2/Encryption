board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True                   #if no square is empty then recursive function breaks
    else:
        row, col = find               # row, col = i,j fromm find_empty function
    for i in range(1,10):
        if valid(bo, i, (row,col)):   # Calling the vlaid function to check if the value entered is valid
            bo[row][col] = i
            if solve(bo):             #recursive function call
                return True
            bo[row][col] = 0
    return False

def valid(bo, num, pos):
    #Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] and pos[0] == i:
            return False
    #Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:        # print horizontal line after every third row
            print("-------------------------")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)                # return row, col
    return None
solve(board)
print_board(board)
