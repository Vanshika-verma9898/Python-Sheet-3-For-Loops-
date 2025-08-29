# 1 2 3 4 
# 1 2 3
# 1 2
# 1

n = int(input("Enter no. of rows : "))
count = 0
for i in range(0, n+1): 
    count = 0
    for j in range(n-i):
        count += 1
        print(count, end=" ")
    print()