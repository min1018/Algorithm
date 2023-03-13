import sys
input = sys.stdin.readline

n = int(input())

a = 0
b = 1
temp = 0
if n != 1:
    for i in range(n-1):
        temp = 0
        temp = a+b
        b = a
        a= temp
                
print(a+b)