import heapq

k = int(input())
n = int(input())
arr = list(map(int, input().strip().split()))

arr.sort()
a = arr[n-1]-arr[0]
tempmin = arr[0]
tempmax = arr[n-1]
for i in range(1, n):
    if (arr[i] >= k):
        tempmin = min(arr[0]+k, arr[i]-k)
        tempmax = max(arr[n-1]-k, arr[i-1]+k)
    a = min(a, tempmax-tempmin)
print(a)
