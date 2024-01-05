n, c = 8, 110
goods = [
    [1, 11],
    [11, 21],
    [21, 31],
    [23, 33],
    [33, 43],
    [43, 53],
    [45, 55],
    [55, 65]
]

max_V, now_W, now_V, best_X, x = 0, 0, 0, [], [0] * n  # 初始化变量# 最大价值、当前重量、当前价值、最优解、商品列表


x = [0 for i in range(n)]  # 初始化当前解

def backtrack(i):  # i是层数，n个物品，共有n+1层
    global max_V, now_V, now_W, best_X, x  # 引入全局变量
    if i >= n:  # 当层数超过物品总数量的时候
        if max_V < now_V:  # 当最大值小于当前价值时，更新最大值
            max_V = now_V
            best_X = x[:]  # 同步更新最优解
    else:
        if now_W + goods[i][0] <= c:  # 如果当前重量加上该层对应物品的重量，可以装在背包里
            x[i] = 1  # 那么就装入这个物品（当前物品的状态为1）
            now_W += goods[i][0]  # 更新当前重量和价值
            now_V += goods[i][1]
            backtrack(i + 1)  # 进入下一个节点（如果符合条件就到底了）
            now_W -= goods[i][0]  # 另一侧节点
            now_V -= goods[i][1]
        x[i] = 0  # 初始化物品状态
        backtrack(i + 1)  # 进入下一层


backtrack(0)  # 从第0层开始搜索
print(f'最大价值为：{max_V}')
print(f'应装物品编号为：{[i + 1 for i in range(n) if best_X[i]]}')
# 3 50
# pls：第1个物品的重量和价值，空格隔开
# 45 50
# pls：第2个物品的重量和价值，空格隔开
# 25 30
# pls：第3个物品的重量和价值，空格隔开
# 25 30