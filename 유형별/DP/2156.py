import sys
input = sys.stdin.readline

n = int(input())
cups = [int(input()) for i in range(n)]
ans = [0]*n

ans[0] = cups[0]
if n>1:
    ans[1] = cups[0]+cups[1]
    
if n>2:
    ans[2] = max(cups[2]+ cups[1], cups[2]+cups[0], ans[1])
    
for i in range(3,n):    
    ans[i] = max(ans[i-2]+cups[i], ans[i-3]+cups[i-1]+cups[i], ans[i-1])
    
print(ans[n-1])