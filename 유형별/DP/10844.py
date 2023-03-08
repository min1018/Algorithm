import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]* 10 for i in range(n+1)]

for i in range(1,10):
    dp[1][i] = 1
    
for i in range(2,n+1):
    for k in range(10):
        #뒤
        if k == 0:
            dp[i][k] = dp [i-1][1]
        elif 2<= k<=8:
            dp[i][k] = dp[i-1][k-1] + dp[i-1][k+1]
        else:
            dp[i][k] = dp[i-1][8]
            
print(sum(dp[n]) % 1000000000)            