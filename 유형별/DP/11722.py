import sys
input = sys.stdin.readline

n = int(input())
temp = list(map(int, input().strip().split()))
dp = [1]*n

for i in range(n):
    for k in range(i):
        if temp[i] < temp[k]:
            dp[i] = max(dp[i], dp[k]+1)
            
print(max(dp))