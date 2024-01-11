def nhap():
    L=[]
    x=int(input())
    n=int(input())
    for i in range(1,n+1):
        i=int(input())
        L.append(i)
    return L,x
    
def search(L,x):
    if x in L:
        for j in range(len(L)):
            if L[j]==x:
                return j
    else:
        return None

L,x=nhap()
print(search(L,x))