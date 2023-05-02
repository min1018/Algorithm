import sys
input = sys.stdin.readline

arr = [1, 1, 1, 2 ,2, 3, 4, 5]

n = int(input())
temp = [int(input()) for i in range(n)]

for i in temp:
    arr = [1, 1, 1, 2 ,2, 3, 4, 5]
    for k in range(7 ,i+2):
        arr.append(arr[k-1] + arr[k-5])

print(arr)
for i in temp:
    print(arr[i+1])