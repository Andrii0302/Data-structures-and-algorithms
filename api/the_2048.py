from random import randint
def start_game():
    matrix=[[0 for i in range(4)] for i in range(4)]
    #print('The rules')
    add_two(matrix)
    return matrix

def add_two(matrix):
    i=randint(0,3)
    j=randint(0,3)
    while matrix[i][j] !=0:
        i=randint(0,3)
        j=randint(0,3)
    matrix[i][j]=2

def printing(matrix):
    for i in range(4):
        for j in range(4):
            print(str(matrix[i][j]).rjust(4),end='')
        print()

def current_state(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==2048:
                return 'You won!'
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==0:
                return 'Not over'
    for i in range(3):
        for j in range(3):
            if matrix[i][j]==matrix[i+1][j] or matrix[i][j]==matrix[i][j+1]:
                return 'Not over'
    for j in range(3):
        if matrix[3][j]==matrix[3][j+1]:
            return 'Not over'
    for i in range(3):
        if matrix[i][3] == matrix[i+1][3]:
            return 'Not over'
    return 'LOST'
def move_up(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    def upward(rows,cols):
        for j in range(cols):
            index = 0  
            for i in range(rows):
                if matrix[i][j] != 0:
                    matrix[index][j] = matrix[i][j]
                    if index != i:
                        matrix[i][j] = 0
                    index += 1
    upward(rows,cols)
    for j in range(cols):
        for i in range(1, rows):
            if matrix[i][j] == matrix[i - 1][j]:
                matrix[i - 1][j] *= 2
                matrix[i][j] = 0
                break
    upward(rows,cols)
    return matrix
def move_down(matrix):
    matrix=matrix[::-1]
    move_up(matrix)
    matrix=matrix[::-1]
    return matrix

def left(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    def lefts(rows,cols):
        for i in range(rows):
            index = 0
            for j in range(cols):
                if matrix[i][j] != 0:
                    matrix[i][index] = matrix[i][j]
                    if index != j:
                        matrix[i][j] = 0
                    index += 1
    lefts(rows,cols)
    for i in range(rows):
        for j in range(1, cols):
            if matrix[i][j] == matrix[i][j - 1]:
                matrix[i][j - 1] *= 2
                matrix[i][j] = 0
                break
    lefts(rows,cols)
    return matrix
def right(matrix):
    rows = len(matrix)
    for i in range(rows):
        matrix[i]=matrix[i][::-1]
    left(matrix)
    for i in range(rows):
        matrix[i]=matrix[i][::-1]






