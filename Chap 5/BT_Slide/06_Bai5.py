def nhap():
    L=[]
    x=int(input())
    y=int(input())
    n=int(input())
    for i in range(1,n+1):
        i=int(input())
        L.append(i)
    return L,x,y

def replace(L,x,y):
    for i in range(len(L)):
        if L[i]==x:
            L[i]=y
    return L

L,x,y=nhap()
print(replace(L,x,y))