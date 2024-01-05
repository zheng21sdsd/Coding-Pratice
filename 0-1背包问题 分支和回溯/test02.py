# # max_V,now_W,now_V,best_X,goods = 0,0,0,[],[]
# ##最大价值 当前重量 当前价值 最优解 商品
# n,c = map(int,input().split())
# for i in range(n):
#     print(f'pls：第{i+1}个物品的重量和价值，空格隔开')
#     goods.append(list(map(int,input().split())))
# x = [0 for i in range(n)] ## 初始化当前解
#
#
#                  1
#         2               2
#      3     3        3       3
#     4  4 4   4    4    4 4     4

#
# max_V, now_W, now_V, best_X, goods = 0, 0, 0, [], []  # 最大价值、当前重量、当前价值、最优解、商品列表
# print('请输入物品数量、背包容积，空格隔开：')
# n, c = map(int, input().split())
# for i in range(n):
#     print(f'请输入第{i + 1}个物品的重量和价值，空格隔开：')
#     goods.append(list(map(int, input().split())))
# x = [0 for i in range(n)]  # 初始化当前解
#
# def backtrack(i, path):  # i是层数，n个物品，共有n+1层
#     global max_V, now_V, now_W, best_X, x  # 引入全局变量
#     if i >= n:  # 当层数超过物品总数量的时候
#         if max_V < now_V:  # 当最大值小于当前价值时，更新最大值
#             max_V = now_V
#             best_X = x[:]  # 同步更新最优解
#             print(f'当前最优解路径：{path}')
#     else:
#         if now_W + goods[i][0] <= c:  # 如果当前重量加上该层对应物品的重量，可以装在背包里
#             x[i] = 1  # 那么就装入这个物品（当前物品的状态为1）
#             now_W += goods[i][0]  # 更新当前重量和价值
#             now_V += goods[i][1]
#             backtrack(i + 1, path + [i + 1])  # 进入下一个节点（如果符合条件就到底了）
#             now_W -= goods[i][0]  # 另一侧节点
#             now_V -= goods[i][1]
#         x[i] = 0  # 初始化物品状态
#         backtrack(i + 1, path)  # 进入下一层
#
# backtrack(0, [])  # 从第0层开始搜索
# print(f'最大价值为：{max_V}')
# print(f'应装物品编号为：{[i + 1 for i in range(n) if best_X[i]]}')


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

max_V, now_W, now_V, best_X, x = 0, 0, 0, [], [0] * n  # 初始化变量

def backtrack(i, path):  # i是层数，n个物品，共有n+1层
    global max_V, now_V, now_W, best_X, x  # 引入全局变量
    if i >= n:  # 当层数超过物品总数量的时候
        if max_V < now_V:  # 当最大值小于当前价值时，更新最大值
            max_V = now_V
            best_X = x[:]  # 同步更新最优解
            print(f'Optimal Solution: {" ".join(map(str, best_X))}')
            print(f'Total Value: {max_V}\n')

    else:
        if now_W + goods[i][0] <= c:  # 如果当前重量加上该层对应物品的重量，可以装在背包里
            x[i] = 1  # 那么就装入这个物品（当前物品的状态为1）
            now_W += goods[i][0]  # 更新当前重量和价值
            now_V += goods[i][1]
            path.append(1)
            print(f'Path: {" ".join(map(str, path))}')
            print(f'Total Weight: {now_W}, Total Value: {now_V}')
            backtrack(i + 1, path)  # 进入下一个节点（如果符合条件就到底了）
            now_W -= goods[i][0]  # 另一侧节点
            now_V -= goods[i][1]
            path.pop()
        x[i] = 0  # 初始化物品状态
        path.append(0)
        backtrack(i + 1, path)  # 进入下一层
        path.pop()

backtrack(0, [])  # 从第0层开始搜索
print('*****'*9)
print(f'最大价值为：{max_V}')
print(f'Total Value: {max_V}\n')
print(f'Optimal Solution: {" ".join(map(str, best_X))}')
print(f'应装物品编号为：{[i + 1 for i in range(n) if best_X[i]]}')

##类似于 图的dfs  图上有环  所以加个备忘录  即可以  和树dfs相比  图的dfs就是背一个备忘录
# 搜索问题  暴力穷举
## 接函数 越来越大  代价函数 越来越小
# 预处理1  按照单价排序好
## 搜索方式  数据结果  深度优秀 用递归来  /处理  广度优先  用优先队列处理
### 对成型 可以帮我们假话工作量