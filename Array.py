# ================ Array =========================
# Reverse array 

arr = [1,2,3,4]

rev_arr = arr[::-1]
print(rev_arr)

# Swapping
def reverarry(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end -=1
    print(arr)

arr = [1,2,3,4]    
reverarry(arr,0,len(arr)-1)

# Reverse inbuilt

arr.reverse()
print(arr)

# ======================================================

# Largest element in array 

arr = [1,3,7,2,5]
print(max(arr))
print(min(arr))
max_element = 0
for i in range(len(arr)-1):
    if arr[i] > max_element:
        max_element = arr[i]
print(max_element)

mini = arr[0]

for i in range(len(arr)-1):
    if arr[i]<mini:
        mini = arr[i]
print(mini)

# =============================================================
# Sum of elements in array 

sum = 0
for i in range(len(arr)):
    sum+=arr[i]
print(sum)

print(sum(arr))

# Recursive approach
def Sumarr(arr,n):
    if n  == 0:
        return False
    return arr[n-1] + Sumarr(arr,n-1)
print(Sumarr(arr,len(arr)))
# ==============================================================
# Sorting

arr = [1,3,7,2,5]
print(sorted(arr))
arr.sort(reverse=True)
print(arr)

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] =temp
print(arr)
# =============================================================
# Count the frequency of the element in array 
a = [1,2,3,1,1,5,7,2,5]
n =len(a)

visited = [False for i in range(n)]
for i in range(n):
    if (visited[i] == True):
        continue
    count =1
    for j in range(i+1,n):
        if a[i] == a[j]:
            visited[j] = True
            count+=1
    print(a[i],":",count)

# Using Hashmap
mp = dict()
for i in range(n):
    if a[i] in mp.keys():
        mp[a[i]] +=1
    else:
        mp[a[i]] = 1
    
for x in mp:
    if mp[x]!=1:
        print(x,":",mp[x])
# ==============================================================
#  Block Swap 
def leftswap(arr,d,n):
    if (d == 0 or d == n):
        return;
    i =d
    j=n-d
    while(i!=j):
        if(i<j):
            swap(arr,d-i,d+j-i,i)
            j-=i
        else:
            swap(arr,d-i,d,j)
            i -= j
        swap(arr,d-i,d,i)
    
def swap(arr,fi,si,d):
    for i in range(d):
        temp = arr[fi+i]
        arr[fi+i] = arr[si+i]
        arr[si+i] = temp
arr  =[1,2,3,4,5,6,7]
leftswap(arr,2,7)

for i in range(7):
    print(arr[i],end="")

# =============================================================

arr  =[1,2,3,4,5,6,7]
temp =arr[0]
n=len(arr)
for i in range(n-1):
    arr[i] = arr[i+1]
arr[n-1] =temp
print(arr)

output = [2, 3, 4, 5, 6, 7, 1]
# ==============================================================
# Find pairs 
def findpairs(pairs) :
    s =set()
    for(x,y) in pairs:
        s.add((x,y))

        if (y,x) in s:
            print((x,y))
pairs = [(3,4),(1,2),(6,7),(4,3)]
findpairs(pairs)
# =============================================================

def duplicate_search(arr):
    dictt = dict()
    if len(arr)<2:
        return False;
    else:
        for i in range(len(arr)):
            if arr[i] in dictt:
                return True
            else:
                dictt[arr[i]] =True
    return False
arr = [1,2,3,1]
print(duplicate_search(arr))