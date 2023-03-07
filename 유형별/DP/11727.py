import sys
input = sys.stdin.readline

n = int(input())
temp = [1,3]

if n > 2:
    for i in range(2, n+1):
        temp.append(temp[i-1] + temp[i-2] * 2)

print(temp[n-1]%10007)