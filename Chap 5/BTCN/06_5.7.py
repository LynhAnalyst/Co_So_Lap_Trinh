def Input():
    L=[]
    n=int(input('n='))
    for i in range(1,n+1):
        i=int(input())
        L.append(i)
    return L

def loaibo(L):
    M=[]
    for i in L:
        if i not in M:
            M.append(i)
    for i in M:
        print(i,end=' ')
    
L=Input()
loaibo(L)