size = 5

def check(board, i, j):
    a = i > -1 and i < size and j > -1 and j < size

    if (a == False): return False
    # print(i, j)
    
    return a and board[i][j] == 0

def possible_moves(board, i, j):
    moves = []

    if check(board, i - 2, j - 1):
        moves.append([i - 2, j - 1])

    if check(board, i - 2, j + 1):
        moves.append([i - 2, j + 1])

    if check(board, i - 1, j + 2):
        moves.append([i - 1, j + 2])

    if check(board, i + 1, j + 2):
        moves.append([i + 1, j + 2])

    if check(board, i + 2, j + 1):
        moves.append([i + 2, j + 1])

    if check(board, i + 2, j - 1):
        moves.append([i + 2, j - 1])

    if check(board, i + 1, j - 2):
        moves.append([i + 1, j - 2])

    if check(board, i - 1, j - 2):
        moves.append([i - 1, j - 2])

    return moves


def check_if_complete(board, count, x, y):
    print(count)
    if (count == size * size): return True

    moves = possible_moves(board, x, y)
    
    for move in moves:
        _x = move[0]
        _y = move[1]

        board[_x][_y] = count

        if (check_if_complete(board, count + 1, _x, _y)):
            return True
        else:
            board[_x][_y] = 0

    return False

    
def knights_tour(board, x = 0, y = 0):
    moves = possible_moves(board, x, y)
    
    if len(moves) == 0: return

    board[0][0] = 1

    if check_if_complete(board, 2, x, y):
        return True
    else: return False


def make_board():
    board = []

    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        board.append(row)

    return board

board = make_board()
print(board)

knights_tour(board)

def print_matrix(matrix):
    for i in range(size):
        for j in range(size):
            if j == size - 1:
                print(matrix[i][j])
            else:
                print(matrix[i][j], end="   |   ")
        print('--------' * size)

    print("\n")

print_matrix(board)