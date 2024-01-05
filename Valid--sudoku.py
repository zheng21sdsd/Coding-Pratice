def check_l(l,r,board):#l :line r:row
    for captcha_l in range(0, 9):
        if captcha_l != l:
            if board[l][r] == board[l][captcha_l]:
                return False
def check_r(l,r,board):#l :line r:row
    for captcha_r in range(0, 9):
        if captcha_r != r:
            if board[l][r] == board[captcha_r][r]:
                return False
                
def check_nine(l,r,board):
###确定l的左边界 和右边界 确定r的左边界和右边界
    templ_r = 0###line 的右边节
    templ_l = 0
    tempr_r = 0###row 的右边节
    tempr_l = 0
    for i in range(0,9,3):
        if i>l:
            templ_r = i
            break
    templ_l = templ_r-3
  
    for i in range(0,9,3):
        if i>r:
            tempr_r = i
            break
    templ_l = tempr_r-3
    
            
    if templ_l<=l<templ_r and tempr_l <=r <templ_r:
        for L in range(templ_l,templ_r):
            for R in range(tempr_l,templ_r):
                if l != L and r !=R:
                    if board[l][r] == board[L][R]:
                        return False
        return True                         
def isValidSudoku(board):
        line = len(board)
        row = len(board[0])
        for l in range(line):
            for r in range(row):
                ###验证行和列是否符合要求
                if not (check_l(l,r,board) and check_r(l,r,board) and check_nine(l,r,board)):
                    return False
        else:
            return True
            
print(isValidSudoku[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])