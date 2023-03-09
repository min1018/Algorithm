from itertools import combinations, permutations
import sys
input = sys.stdin.readline

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
n = int(input())
ans = 10
for i in range(2,n+1):
    if i == n:
        ans += len(list(combinations(nums,i)))
    else:
        ans += len(list(combinations(nums, i))) * i
    
print(ans%10007)