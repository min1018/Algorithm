import sys
input = sys.stdin.readline

n = int(input())
ans = []
for i in range(n):
    k = int(input()) 
    l1 = list(map(int, input().strip().split(" ")))
    l2 = list(map(int, input().strip().split(" ")))
    for i in range(1,k):
        if i ==1:
            l1[i] = l2[i-1]+l1[i]
            l2[i] = l1[i-1]+l2[i]
        else:
            l1[i] = max(l2[i-1], l2[i-2])+l1[i]
            l2[i] = max(l1[i-1], l1[i-2])+l2[i]
            if i ==k-1 :
                ans.append(max(l1[i], l2[i]))    
                
for i in range(n):
    print(ans[i])