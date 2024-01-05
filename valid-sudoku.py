# 函数定义
# def check_l(l, r, board):  # l :line r:row
#     for captcha_l in range(0, 9):
#         if captcha_l != r:
#             if board[l][r] == board[l][captcha_l]:
#                 print('xxxxxx')
#                 return False
#     return True
# def check_r(l, r, board):  # l :line r:row
#     for captcha_r in range(0, 9):
#         if captcha_r != l:
#             if board[l][r] == board[captcha_r][r]:
#                 print('xxx')
#                 return False
#     return True
# def check_nine(l, r, board):
#     ###确定l的左边界 和右边界 确定r的左边界和右边界
#     templ_r = 0  ###line 的右边节
#     templ_l = 0
#     tempr_r = 0  ###row 的右边节
#     tempr_l = 0
#     for i in range(0, 12, 3):
#         if i > l:
#             templ_r = i
#             break
#     templ_l = templ_r - 3
#
#     for i in range(0, 12, 3):
#         if i > r:
#             tempr_r = i
#             break
#     tempr_l = tempr_r - 3
#
#     if templ_l <= l < templ_r and tempr_l <= r < tempr_r:
#         for L in range(templ_l, templ_r):
#             for R in range(tempr_l, tempr_r):
#                 if l != L and r != R :
#                     if board[l][r] == board[L][R] and board[l][r] != '.':
#                         print('check_nine')
#                         return False
#
#         return True
#
#
# def isValidSudoku(board):
#     line = len(board)
#     row = len(board[0])
#     for l in range(line):
#         for r in range(row):
#             ###验证行和列是否符合要求
#             if board[l][r] != '.':
#                 if not (check_l(l, r, board) and check_r(l, r, board) and check_nine(l, r, board)):
#                     return False
#     else:
#         return True
###############################################
# 类代码
# class Solution(object):
#     def check_l(self,l, r, board):  # l :line r:row
#         for captcha_l in range(0, 9):
#             if captcha_l != r:
#                 if board[l][r] == board[l][captcha_l]:
#                     print('xxxxxx')
#                     return False
#         return True
#     def check_r(self,l, r, board):  # l :line r:row
#         for captcha_r in range(0, 9):
#             if captcha_r != l:
#                 if board[l][r] == board[captcha_r][r]:
#                     print('xxx')
#                     return False
#         return True
#     def check_nine(self,l, r, board):
#         ###确定l的左边界 和右边界 确定r的左边界和右边界
#         templ_r = 0  ###line 的右边节
#         templ_l = 0
#         tempr_r = 0  ###row 的右边节
#         tempr_l = 0
#         for i in range(0, 12, 3):
#             if i > l:
#                 templ_r = i
#                 break
#         templ_l = templ_r - 3
#
#         for i in range(0, 12, 3):
#             if i > r:
#                 tempr_r = i
#                 break
#         tempr_l = tempr_r - 3
#
#         if templ_l <= l < templ_r and tempr_l <= r < tempr_r:
#             for L in range(templ_l, templ_r):
#                 for R in range(tempr_l, tempr_r):
#                     if l != L and r != R :
#                         if board[l][r] == board[L][R] and board[l][r] != '.':
#                             print('check_nine')
#                             return False
#
#             return True
#
#
#     def isValidSudoku(self,board):
#         line = len(board)
#         row = len(board[0])
#         for l in range(line):
#             for r in range(row):
#                 ###验证行和列是否符合要求
#                 if board[l][r] != '.':
#                     if not (Solution().check_l(l, r, board) and Solution().check_r(l, r, board) and Solution().check_nine(l, r, board)):
#                         return False
#         else:
#             return True
#
#
# print(Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
# , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
# , [".", "9", "8", ".", ".", ".", ".", "6", "."]
# , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
# , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
# , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
# , [".", "6", ".", ".", ".", ".", "2", "8", "."]
# , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
# , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))


class Solution(object):
    def isValidSudoku(self,board):
        line = len(board)
        row = len(board[0])
        for l in range(line):
            storage_L = []##行判断
            storage_R = []###列判断
            for r in range(row):
                ###进行 行判断
                if  board[l][r] == '.':
                    continue
                if board[l][r] not in storage_L:
                    storage_L.append(board[l][r])
                else:
                    return False
                ###进行 列判断
                if  board[r][l] == '.':
                    continue
                if board[r][l] not in storage_R:
                    storage_R.append(board[r][l])
                else:
                    return False
        ### 进行九宫格判断 行 0+line~3+line  列 0+row~3+row  line 0，3，6row 0，3，6
        for line in range(0,9,3):
            for row in range(0,9,3):
                storage_Nine = []
                for l in range(0,3):
                    for r in range(0,3):
                        if board[r+line][l+row] == '.':
                            continue
                        if board[r+line][l+row] not in storage_Nine:
                            storage_Nine.append(board[r+line][l+row])
                        else:
                            return False

        return True
print(Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
, ["6", ".", ".", "1", "9", "5", ".", ".", "."]
, [".", "9", "8", ".", ".", ".", ".", "6", "."]
, ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
, ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
, ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
, [".", "6", ".", ".", ".", ".", "2", "8", "."]
, [".", ".", ".", "4", "1", "9", ".", ".", "5"]
, [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))