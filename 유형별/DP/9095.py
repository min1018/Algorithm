import sys
input = sys.stdin.readline

temp = [1,2,4]

n = int(input())
ans = [int(input()) for i in range(n)]

for i in range(3, max(ans)+1):
    temp.append(temp[i-1]+temp[i-2]+temp[i-3])
    
for i in range(n):
    print(temp[ans[i]-1])