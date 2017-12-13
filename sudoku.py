import math
import random

def read_sudoku(filename):
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(values):
    for i in range(9):
        print(value[i][0], value[i][1], value[i][2], "|",
              value[i][3], value[i][4], value[i][5], "|",
              value[i][6], value[i][7], value[i][8])
        if(i == 2) or (i == 5):
            print("------+-------+------")
    print()


def group(values, n):
    Matrix = []
    For i in range(len(values) // n)
        For j in range(n * i: n * i + n)
    Matrix.append([])
    Matrix = matrix[i].append(j)
    return Matrix


def get_row(values, pos):
    return(values[pos[0]])


def get_col(values, pos):
    numb = []
    for i in range(9):
        numb.append(values[i][pos[1]])
    return numb


def get_block(values, pos):
    numb = []
    a, b = pos[0] // 3, pos[1] // 3
    for i in range(3):
        numb.append(values[a*3 + i][b*3:b*3+3])
    return numb


def find_empty_positions (grid):
    for i in range(len(grid)):
        if (grid[i].count(".") != 0):
            return (i, grid[i].index("."))
    return ()


def find_possible_values (grid, pos):
    numb = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row = get_row(grid, pos)
    col = get_col(grid, pos)
    block = get_block(grid, pos)
    for i in range(1, 10):
        if str(i) in row:
            numb.remove(i)
            continue
        if str(i) in col:
            numb.remove(i)
            continue
        for k in range(3):
            if str(i) in block[k]:
                numb.remove(i)
    return numb


def solve(grid):
    b = find_empos(grid)
    if b == ():
        return grid
    else:
        a = find_posval(grid, b)
        if a == []:
            return None
        for i in a:
            grid[b[0]][b[1]] = str(i)
            s = solve(grid)
            if s is not None:
                return grid
    grid[b[0]][b[1]] = "."


def check_solution(grid):
    et = set([str(i) for i in range(1,10)])
    for j in range(9):
        row = set(get_row(grid, (j, 0)))
        col = set(get_col(grid, (0, j)))
        if row != et:
            return False
        if col != et:
            return False
    for j in range(3):
        for k in range(3):
            block = set(get_block(grid,(j*3, k*3))[0] + get_block(grid,(j*3, k*3))[1] + get_block(grid,(j*3, k*3))[2])
            if block != et:
                return False
    return True
 

def generate(n):
    a = read_sudoku("s.txt")  
    b = [(0,0), (1,3), (3,1), (4,4), (5,7), (7,5), (2,6), (6,2), (8,8)]
    for pair in b:
        a[pair[0]][pair[1]]=str(random.randrange(1,10))
    a = solve(a)
    a = dele(a,n)
    return a

