import sys
input = sys.stdin.readline

n = int(input())
temp = list(map(int, input().strip().split(" ")))
print(temp)
dp = [0] * n
for i in range(1,n):
    for k in range(0,i):
        if temp[i]>temp[k]:
            dp[i] = max(dp[i],dp[k]+1)
            
print(max(dp))