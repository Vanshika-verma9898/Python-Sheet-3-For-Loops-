# * * * * * 
#  * * * *
#   * * *
#    * *
#     *

n = int(input("Enter no. of rows : "))

for i in range(0,n):
    for j in range(i):
        print(' ',end="")
    for k in range(n-i):
        print('*',end=" ")
    print()