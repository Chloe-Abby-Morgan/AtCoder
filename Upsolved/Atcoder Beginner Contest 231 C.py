N,Q = map(int, input().split())
A = input().split()
X = []

for i in range(Q):
    X.append(input())

A.sort()

def binarySearch(arr, target):

    if target <= arr[0]:
        return len(arr)

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target and arr[mid-1] < target:
            return len(arr) - mid
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0

for i in X:
    print(binarySearch(A, i))