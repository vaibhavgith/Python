# ================== Bubble Sort ====================
a= [7, 3, 9, 12, 11]
n = len(a)
for i in range(n-1):
    Swapped =False
    for j in range(n-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
        Swapped =True
    if not Swapped:
        break

print("Sorted array", a)

# ======================= Selection Sort =================
a= [7, 3, 9, 12, 11]
n=len(a)
# Using shifting it requires more time as in background shifting operation are peeformming
for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
        if a[j]<a[min_index]:
            min_index = j
    min_value = a.pop 
    a.insert(i,min_value)

print(a)

# Using swapping elements it will save time as compare to shifting

for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
        if a[j]<a[min_index]:
            min_index = j
    a[i],a[min_index] = a[min_index],a[i]
print (a)

# ==========================Insertion Sort======================================
a= [7,12,9,11,3]
n = len(a)
for i in range(1,n):
    current_index  =i
    current_value = a.pop(i)
    for j in range(i-1,-1,-1):
        if a[j]>current_value:
            current_index = j
    a.insert(current_index,current_value)
print(a)

# Better solution
for i in range(1,n):
    current_index  =i
    current_value = a[i]
    for j in range(i-1,-1,-1):
        if a[j]>current_value:
            a[j+1] = a[j]
            current_index = j
        else:
            break

    a[current_index] =current_value
print(a)

# ==========================Quick Sort===========================================

def partition(array,low,high):
    pivot = array[high]
    i = low -1

    for j in range(low,high):
        if array[j]<=pivot:
            i+=1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[high] = array[high],array[i+1]
    return i+1

def quicksort(array, low = 0, high = None):
    if high is None :
        high = len(array)-1
    if low < high:
        pivot_index = partition(array,low,high)
        quicksort(array,low,pivot_index-1)
        quicksort(array,pivot_index+1,high)

array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(array)
print(array)

def quick_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose a pivot (typically the last element)
        pivot = arr[-1]
        # Partition the array into two parts: less than and greater than pivot
        less_than_pivot = [x for x in arr[:-1] if x <= pivot]
        greater_than_pivot = [x for x in arr[:-1] if x > pivot]
        # Recursively sort the partitions and combine them
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
# =====================Merge Sort=================================================================
def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    leftsort = mergesort(lefthalf)
    rightsort = mergesort(righthalf)

    return merge(leftsort,rightsort)

def merge(left,right):
    result = []
    i = j =0

    while i < len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])

    return result
    
arr = [8,12,5,9,11,45]
sorted = mergesort(arr)
print(sorted)

# =========================Counting Sort =================================================
def countingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr

unsortedArr = [8,12,5,6,7,2,3]
sortedArr = countingSort(unsortedArr)
print("Sorted array:", sortedArr)