class Board:
    def __init__(self, n):
        self.n = n
        self.board = [['.' for _ in range(n)] for __ in range(n)]

    def is_valid_move(self, row, col):
        col_j = col
        left_diag_j = col
        right_diag_j = col
        for i in range(row, -1, -1):
            if self.board[i][col_j] == 'Q':
                return False
            if left_diag_j >= 0 and self.board[i][left_diag_j] == 'Q':
                return False
            if right_diag_j < self.n and self.board[i][right_diag_j] == 'Q':
                return False
            left_diag_j -= 1
            right_diag_j += 1
        return True

    def place_queen(self, row, col):
        self.board[row][col] = 'Q'

    def remove_queen(self, row, col):
        self.board[row][col] = '.'

    def output_format(self):
        return [''.join(row) for row in self.board]


def solve_queens(n):
    output = []
    board = Board(n)
    def dfs(row):
        if row == n:
            output.append(board.output_format())
            return
        for col in range(n):
            if board.is_valid_move(row, col):
                board.place_queen(row, col)
                dfs(row+1)
                board.remove_queen(row, col)
    dfs(0)
    return output


print(solve_queens(4))

