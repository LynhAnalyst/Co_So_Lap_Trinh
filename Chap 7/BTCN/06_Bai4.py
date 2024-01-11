str=input().split(',')
L=[]
for i in str:
    if i not in L:
        L.append(i)
L.sort()
        
print(','.join(L))