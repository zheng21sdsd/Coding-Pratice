n = int(input())
numbers = list(map(int, input().split()))
dp = []

for i in range(n):
    res = []
    resu = 0
    for j in range(i, -1, -1):
        resu += numbers[j]
        res.append(resu)

    max_val = res[0]
    for z in range(len(res)):
        if res[z] > max_val:
            max_val = res[z]

    dp.append(max_val)

max_val = dp[0]
for i in range(len(dp)):
    if dp[i] > max_val:
        max_val = dp[i]

print(max_val)
