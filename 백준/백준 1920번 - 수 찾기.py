import sys
n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

arr1.sort()
for i in arr2:
    if binary_search(arr1, i, 0, n-1) == None:
        print("0")
    else:
        print("1")
