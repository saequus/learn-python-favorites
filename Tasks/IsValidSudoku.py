from collections import defaultdict
class Solution1(object):
    def searchInsert(self, board):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        stack_column = defaultdict(list)
        stack_squares = defaultdict(list)
        for i in range(len(board)):
            stack_row = []
            for j in range(len(board[i])):
                if board[i][j].isdigit():
                    number = board[i][j]

                    if number in stack_row:
                        return False
                    else:
                        stack_row.append(number)

                    if number in stack_column[j]:
                        return False
                    else:
                        stack_column[j].append(number)

                    if i < 3 and j < 3:
                        if number in stack_squares[1]:
                            return False
                        else:
                            stack_squares[1].append(number)

                    if i < 3 and 2 < j < 6:
                        if number in stack_squares[2]:
                            return False
                        else:
                            stack_squares[2].append(number)

                    if i < 3 and 5 < j < 9:
                        if number in stack_squares[3]:
                            return False
                        else:
                            stack_squares[3].append(number)

                    if 2 < i < 6 and j < 3:
                        if number in stack_squares[4]:
                            return False
                        else:
                            stack_squares[4].append(number)

                    if 2 < i < 6 and 2 < j < 6:
                        if number in stack_squares[5]:
                            return False
                        else:
                            stack_squares[5].append(number)

                    if 2 < i < 6 and 5 < j < 9:
                        if number in stack_squares[6]:
                            return False
                        else:
                            stack_squares[6].append(number)

                    if 5 < i < 9 and j < 3:
                        if number in stack_squares[7]:
                            return False
                        else:
                            stack_squares[7].append(number)

                    if 5 < i < 9 and 2 < j < 6:
                        if number in stack_squares[8]:
                            return False
                        else:
                            stack_squares[8].append(number)

                    if 5 < i < 9 and 5 < j < 9:
                        if number in stack_squares[9]:
                            return False
                        else:
                            stack_squares[9].append(number)

        return True



class Solution:
    def isValidSudoku(self, board):
        columns = len(board)
        rows = [len(r) for r in board]
        if columns != 9 or min(rows) != 9 or max(rows) != 9:
            return False

        for i in range(9):
            row = board[i]
            col = [board[j][i] for j in range(9)]
            subgrid = [board[j // 3 + 3 * (i // 3)][j % 3 + 3 * (i % 3)] for j in range(9)]
            if self.checkDup(row) is not True or self.checkDup(col) is not True or self.checkDup(subgrid) is not True:
                return False

        return True

    def checkDup(self, l):
        Counter = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
        for i in l:
            if i != ".":
                Counter[i] += 1
                if Counter[i] > 1:
                    return False
        return True


x = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".",".","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".","1",".",".","8",".","2",".","9"]
]



y = [[".",".",".",".",".",".",".",".","."],
     ["3",".",".",".","4","6","5",".","."],
     [".",".","5",".","2",".",".",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".","3",".",".",".",".",".",".","1"],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".","6",".","."],
     [".",".",".",".",".","5",".","6","."],
     [".",".",".","9",".",".",".",".","."]]


# f = Solution1()
# print(f.searchInsert(y))
s = Solution()
print(s.isValidSudoku(x))
print(s.isValidSudoku(y))



# d = defaultdict(list)
# print(d)
# for i in range(len(x)):
#     stack1 = []
#     for j in range(len(x[i])):
#         if x[i][j].isdigit():
#             number = x[i][j]
#             if number in stack1:
#                 print(False)
#             else:
#                 stack1.append(number)
#             if number in d[j]:
#                 print(False)
#             else:
#                 d[j].append(x[i][j])
#     print(True)






