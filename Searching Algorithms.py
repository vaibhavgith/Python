# Searching Algorithms

# 1 . Linear Search
# =================================================
def linersearch(arr,value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i

    return -1

arr = [3,6,9,12,5,8,2]
value =5
found = linersearch(arr,value)
print(found)

# 2.Binary Search
# =========================================================
def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid
        
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15

result = binarySearch(myArray, myTarget)

print(result)