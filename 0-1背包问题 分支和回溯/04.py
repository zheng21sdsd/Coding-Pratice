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

def highest_value_to_weight_ratio(items):
    # Calculate the highest value-to-weight ratio among the items
    max_ratio = 0
    index = -1
    for i, item in enumerate(items):
        ratio = item[1] / item[0]
        if ratio > max_ratio:
            max_ratio = ratio
            index = i
    return max_ratio, index

def upper_bound(i):
    remaining_items = goods[i:]
    sorted_items = sorted(remaining_items, key=lambda item: item[1] / item[0], reverse=True)
    remaining_capacity = c - now_W
    bound = now_V
    for item in sorted_items:
        if item[0] <= remaining_capacity:
            bound += item[1]
            remaining_capacity -= item[0]
        else:
            bound += remaining_capacity * (item[1] / item[0])
            break
    return bound

def backtrack(i, path):
    global max_V, now_V, now_W, best_X, x
    if i >= n:
        if max_V < now_V:
            max_V = now_V
            best_X = x[:]
            print(f'Optimal Solution: {" ".join(map(str, best_X))}')
            print(f'Total Value: {max_V}\n')
    else:
        if now_W + goods[i][0] <= c:
            x[i] = 1
            now_W += goods[i][0]
            now_V += goods[i][1]
            path.append(1)
            print(f'Path: {" ".join(map(str, path))}')
            print(f'Total Weight: {now_W}, Total Value: {now_V}')
            backtrack(i + 1, path)
            now_W -= goods[i][0]
            now_V -= goods[i][1]
            path.pop()
        # Only explore if the upper bound is greater than the current maximum value
        if upper_bound(i) > max_V:
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
