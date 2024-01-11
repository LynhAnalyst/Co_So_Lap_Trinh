def nhap():
    L=[]
    n=int(input())
    for i in range(1,n+1):
        i=int(input())
        L.append(i)
    return L

def count(L):
    s=0
    for i in L:
        s+=1
    return s

L=nhap()
print(count(L))