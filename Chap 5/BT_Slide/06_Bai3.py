def nhap():
    L=[]
    x=int(input())
    n=int(input())
    for i in range(1,n+1):
        i=int(input())
        L.append(i)
    return L,x

def delete(L,x):
    j=1
    while j<len(L):
        if L[j]==x:
            L.pop(j)
        else:
            j+=1 
    return L

L,x=nhap()
print(delete(L,x))