class Board:
    def __init__(self, n):
        self.n = n
        self.board = [['.' for _ in range(n)] for i in range(n)]


    def isValideMove(self, row, col):
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

    def placeQueen(self, row, col):
        self.board[row][col] = 'Q'

    def removeQueen(self, row, col):
        self.board[row][col] = '.'

    def outputFormat(self):
        return [''.join(row) for row in self.board]


def solveQueens(n):
    output = []
    board = Board(n)
    def dfs(row):
        if row == n:
            output.append(board.outputFormat())
            return
        for col in range(n):
            if board.isValideMove(row, col):
                board.placeQueen(row, col)
                dfs(row+1)
                board.removeQueen(row, col)
    dfs(0)
    return output


print(solveQueens(4))

