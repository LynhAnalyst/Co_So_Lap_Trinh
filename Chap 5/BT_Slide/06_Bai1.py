def nhap():
    L=[]
    x=int(input())
    k=int(input())
    n=int(input())
    for i in range(1,n+1):
        i=int(input())
        L.append(i)
    return L,x,k
    
def add(L,x,k):
    if k>len(L):
        L.append(x)
    else:
        L.insert(k,x)
    return L
    
    
L,x,k=nhap()
print(add(L,x,k))
