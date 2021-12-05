def fill_x(board, from_x, y, to_x):
    for x in range(min(from_x, to_x), max(from_x, to_x) + 1):
        board[y][x] = board[y][x] + 1


def fill_no_diagonal(board, from_x, from_y, to_x, to_y):
    if from_y == to_y:
        fill_x(board, from_x, from_y, to_x)
    else:
        for y in range(min(from_y, to_y), max(from_y, to_y) + 1):
            fill_x(board, from_x, y, to_x)


def fill_diagonal(board, from_x, from_y, to_x, to_add_y):
    y = from_y + to_add_y
    x_diff = to_x - from_x
    for to_add_x in range(min(0, x_diff), max(0, x_diff) + 1):
        x = from_x + to_add_x
        if abs(to_add_x) == abs(to_add_y):
            board[y][x] = board[y][x] + 1
