import sys
input = sys.stdin.readline

n = int(input())
temp = list(map(int, input().strip().split(" ")))
dp = [0]*n
dp[0] = temp[0]
for i in range(1,n):
    for k in range(i):
        if temp[i]>temp[k]:
            dp[i] = max(dp[k]+temp[i], dp[i])
        else:
            dp[i] = max(dp[i],temp[i])
print(max(dp))