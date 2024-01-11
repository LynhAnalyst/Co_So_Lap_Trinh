L=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    for j in range(3):
        if L[i][j]%2==0:
            L[i][j]='x'

for row in L:
    print(row)