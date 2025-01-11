# ****
# ****
# ****
# ****
n=4 

for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()

for i in range(n):
    print("*"*n)
# ==================================================
# ****
# *  *
# *  *
# ****
n=4
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
# ======================================================
# ****
#  ****
#   ****
#    ****
n = 4 
for i in range(n):
    while i>0:
        print(" ",end="")
        i-=1
    for i in range(n):
        print("*",end="")
    print()

for i in range(n):
    print(" "*i,"*"*n)
# ===========================================================

#      ****
#     ****
#    ****
#   ****
n= 4
for i in range(n):
    for j in range(i,n+1):
        print(" ",end="")
    for k in range(n):
        print("*",end="")
    print()
# =========================================================
# *
# **
# ***
# ****
n =4
for i in range(n+1):
    for j in range(i):
        print("*",end="")
    print()
# ===========================================================
#     *
#    ***
#   *****
n=4
for i in range(n):
    for j in range(i,n+1):
        print(" ",end="")
    for  k in range(1,i*2):
        print("*",end="")
    print()
# ============================================================
# *******
#  *****
#   ***
#    *
n=5
for i in range(n,1,-1):
    for k in range(0,n-i):
        print(" ",end="")
    for j in range(i,2*i-1):
        print("*",end="")
    for j in range(1,i-1):
        print("*",end="")
    print()
# ==================================================

#      *
#     * *
#    *   *
#   *     *
#  *********
n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i+1):
        if j == 0 or j ==2*i or i == n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
# ========================================================
n =5 
for i in range(0, n):
    for j in range(0, n-i-1):
        print(" ",end="")
    for j in range(0, i*2+1):
        print("*", end="")
    print()

for i in range(1, n):
    for j in range(0, i):
        print(" ",end="")
    for j in range(0, (n-i)*2-1):
        print("*", end="")
    print()
# ==========================================================
