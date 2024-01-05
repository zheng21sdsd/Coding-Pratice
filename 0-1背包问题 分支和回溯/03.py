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

temp = 165.9
max_V, now_W, now_V, best_X, x = 0, 0, 0, [], [0] * n  # 初始化变量

def max_value_to_weight_ratio(items):
    max_price = 0
    for item in items:
        max_price += item[1]
        temp = max_price
    return max_price

def backtrack(i, path):
    global max_V, now_V, now_W, best_X, x,temp
    remaining_items = goods[:i-1]
    if i >= n:
        if max_V < now_V:
            max_V = now_V
            best_X = x[:]
            print(f'Optimal Solution: {" ".join(map(str, best_X))}')
            print(f'Total Value: {max_V}\n')
            print(f'Path: {" ".join(map(str, path))}')
            print(f'Total Weight: {now_W}, Total Value: {now_V},max_value_to_weight_ratio:{max_value_to_weight_ratio(remaining_items)}')
    else:

        if now_W + goods[i][0] <= c:
            x[i] = 1
            now_W += goods[i][0]
            now_V += goods[i][1]
            path.append(1)
            print(f'Path: {" ".join(map(str, path))}')
            print(f'Total Weight: {now_W}, Total Value: {now_V}, Max Value-to-weight ratio: {temp}')
            backtrack(i + 1, path)
            now_W -= goods[i][0]
            now_V -= goods[i][1]
            path.pop()
        # Calculate an upper bound based on the remaining capacity and the maximum value-to-weight ratio


        x[i] = 0
        path.append(0)
        backtrack(i + 1, path)
        path.pop()

backtrack(0, [])  # 从第0层开始搜索
print('*****'*9)
print(f'最大价值为：{max_V}')
print(f'Total Value: {max_V}\n')
print(f'Optimal Solution: {" ".join(map(str, best_X))}')
print(f'应装物品编号为：{[i + 1 for i in range(n) if best_X[i]]}')
