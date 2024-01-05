# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max1 = 0
#         for byout in range(len(prices)-1,-1,-1):
#             for byin in range(byout-1,-1,-1):
#                 if prices[byout]-prices[byin]>0:
#                     max1 = prices[byout]-prices[byin] if prices[byout]-prices[byin]>=max1 else max1
#                 else:
#                     break
#         return max1



# Python3
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min1 = 100000000000000000000000000000
#         max1 = 0
#         for by in range(0, len(prices)):
#             if prices[by] < min1:
#                 min1 = prices[by]
#             elif prices[by] - min1 > max1:
#                 max1 = prices[by] - min1
#         return max1




# def dfs(i, j, board):
#     if i - 1 < 0:
#         return
#     if i + 1 > len(board[0]) - 1:
#         return
#     if j - 1 < 0:
#         return
#     if j + 1 > len(board):
#         return
#     board[i][j] = 'X'
#     if board[i - 1][j] == 'O':
#         dfs(i - 1, j, board)
#     if board[i + 1][j] == 'O':
#         dfs(i + 1, j, board)
#     if board[i][j - 1] == 'O':
#         dfs(i, j - 1, board)
#     if board[i][j + 1] == 'O':
#         dfs(i, j + 1, board)
#
# def mn(board):
#     r = len(board)  # 行
#     l = len(board[0])  # 列
#     for i in range(r):
#         for j in range(l):
#             if board[i][j] == 'O':
#                 dfs(i, j, board)
#     return board

class Solution:
    def dfs(self,i, j, board):
        if i - 1 < 0:
            return
        if i + 1 > len(board) - 1:
            return
        if j - 1 < 0:
            return
        if j + 1 > len(board[0])-1:
            return
        if board[i - 1][j] == 'O' and board[i - 1][j] == 'O' and board[i][j - 1] == 'O' and board[i][j + 1] == 'O':
            return

        if i - 1 != 0 and board[i - 1][j] == 'O':
            board[i][j] = 'X'
            Solution.dfs(self,i - 1, j, board)
        if i+1 != len(board)-1 and board[i+1][j] == 'O':
            board[i][j] = 'X'
            Solution.dfs(self,i + 1, j, board)
        if j-1 != 0 and board[i][j - 1] == 'O':
            board[i][j] = 'X'
            Solution.dfs(self,i, j - 1, board)
        if j+1!= len(board[0])-1 and board[i][j + 1] == 'O':
            board[i][j] = 'X'
            Solution.dfs(self,i, j + 1, board)

    def solve(self, board):
        r = len(board)  # 行
        l = len(board[0])  # 列
        for i in range(r):
            for j in range(l):
                if board[i][j] == 'O':
                    Solution.dfs(self,i, j, board)
        return board
a = Solution()
print(a.solve(board = [["O","O","O"],["O","O","O"],["O","O","O"]]))