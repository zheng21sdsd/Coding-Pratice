import os
import sys


# 请在此输入您的代码

def slove(N,V):
  old=1
  now=0
  for i in range(N+1):
    old,now=now,old
    for j in range(0,V+1):
      if c[i]>j:
        dp[now][j]=dp[old][j]
      else:
        dp[now][j]=max(dp[old][j],dp[old][j-c[i]]+w[i])
  return dp[now][V]

V,N=map(int,input().split())
w=[0]*11000
c=[0]*11000
dp=[[0]*10000 for _ in range(2)]
for i in range(1,N+1):
  c[i],w[i]=map(int,input().split())
print(slove(N,V))

