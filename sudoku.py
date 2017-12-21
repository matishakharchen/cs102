import random

def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(value):
    """Вывод Судоку """
    for i in range(9):
        print(value[i][0], value[i][1], value[i][2], "|",
              value[i][3], value[i][4], value[i][5], "|",
              value[i][6], value[i][7], value[i][8])
        if(i == 2) or (i == 5):
            print("------+-------+------")
    print()


def group(values, n):
    """Сгруппировать значения values в список, состоящий из списков по n элементов
       >>> group([1,2,3,4], 2)
       [[1, 2], [3, 4]]
       >>> group([1,2,3,4,5,6,7,8,9], 3)
       [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
       """
    return [values[i:i + n] for i in range(0, len(values), n)]

def get_row(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos
        >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
        ['1', '2', '.']
        >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
        ['4', '.', '6']
        >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
        ['.', '8', '9']
        """
    return(values[pos[0]])


def get_col(values, pos):
    """ Возвращает все значения для номера столбца, указанного в pos
        >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
        ['1', '4', '7']
        >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
        ['2', '.', '8']
        >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
        ['3', '6', '9']
        """
    numb = []
    for i in range(9):
        numb.append(values[i][pos[1]])
    return numb


def get_block(values, pos):
    """ Возвращает все значения из квадрата, в который попадает позиция pos
        >>> grid = read_sudoku('puzzle1.txt')
        >>> get_block(grid, (0, 1))
        ['5', '3', '.', '6', '.', '.', '.', '9', '8']
        >>> get_block(grid, (4, 7))
        ['.', '.', '3', '.', '.', '1', '.', '.', '6']
        >>> get_block(grid, (8, 8))
        ['2', '8', '.', '.', '.', '5', '.', '7', '9']
        """
    numb = []
    a, b = pos[0] // 3, pos[1] // 3
    for i in range(3):
        numb.append(values[a*3 + i][b*3:b*3+3])
    return numb


def find_empty_positions (grid):
    """ Найти первую свободную позицию в пазле
        >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
        (0, 2)
        >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
        (1, 1)
        >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
        (2, 0)
        """
    for i in range(len(grid)):
        if (grid[i].count(".") != 0):
            return (i, grid[i].index("."))
    return ()


def find_possible_values (grid, pos):
    """ Вернуть множество возможных значения для указанной позиции
        >>> grid = read_sudoku('puzzle1.txt')
        >>> values = find_possible_values(grid, (0,2))
        >>> values == {'1', '2', '4'}
        True
        >>> values = find_possible_values(grid, (4,7))
        >>> values == {'2', '5', '9'}
        True
        """
    number = set('123456789')
    row = set(get_row(grid, pos))
    col = set(get_col(grid, pos))
    block = set(get_block(grid, pos))
    return number - set.union(block, row, col)


def solve(grid):
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    b = find_empty_positions(grid)
    if b == ():
        return grid
    else:
        a = find_empty_positions(grid)
        if a == []:
            return None
        for i in a:
            grid[b[0]][b[1]] = str(i)
            s = solve(grid)
            if s is not None:
                return grid
    grid[b[0]][b[1]] = "."


def check_solution(grid):
    """ Если решение solution верно, то вернуть True, в противном случае False """
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
    """ Генерация судоку заполненного на N элементов
        >>> grid = generate_sudoku(40)
        >>> sum(1 for row in grid for e in row if e == '.')
        41
        >>> solution = solve(grid)
        >>> check_solution(solution)
        True
        >>> grid = generate_sudoku(1000)
        >>> sum(1 for row in grid for e in row if e == '.')
        0
        >>> solution = solve(grid)
        >>> check_solution(solution)
        True
        >>> grid = generate_sudoku(0)
        >>> sum(1 for row in grid for e in row if e == '.')
        81
        >>> solution = solve(grid)
        >>> check_solution(solution)
        True
        """
    a = read_sudoku("s.txt")  
    b = [(0,0), (1,3), (3,1), (4,4), (5,7), (7,5), (2,6), (6,2), (8,8)]
    for pair in b:
        a[pair[0]][pair[1]]=str(random.randrange(1,10))
    a = solve(a)
    a = dele(a,n)
    return a

if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        display(solution)
