def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def remove_queen(row, col, board, rows, cols, left_d, right_g):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left_d.remove(row - col)
    right_g.remove(row + col)


def set_queen(row, col, board, rows, cols, left_d, right_g):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left_d.add(row - col)
    right_g.add(row + col)


def can_place_queen(row, col, rows, cols, left_d, right_g):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in left_d:
        return False
    if (row + col) in right_g:
        return False
    return True


def put_queens(row, board, rows, cols, left_d, right_g):
    if row == 8:
        print_board(board)
        return

    for col in range(8):
        if can_place_queen(row, col, rows, cols, left_d, right_g):
            set_queen(row, col, board, rows, cols, left_d, right_g)
            put_queens(row + 1, board, rows, cols, left_d, right_g)
            remove_queen(row, col, board, rows, cols, left_d, right_g)


n = 8
board = []
[board.append(["-"] * n) for _ in range(8)]

put_queens(0, board, set(), set(), set(), set())