#

# 递归   计算了很多f（1） f（2） f（3） 既有重叠子问题
###定义走楼梯函数climb_stairs
# def climb_stairs(n):
#     if n == 1:
#         return 1
#     if  n == 2:
#         return 2
#     else:
#         return climb_stairs(n-1)+climb_stairs(n-2)
# print(f'共有{climb_stairs(10)}爬法')

### 迭代无重叠子问题
def count_ways(n):
    if n <= 2:
        return n
    else:
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b

ways = count_ways(10)
print(f"10级楼梯有 {ways} 种走法。")
