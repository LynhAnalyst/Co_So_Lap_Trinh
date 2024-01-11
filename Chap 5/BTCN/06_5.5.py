def Input():
    L=[]
    n=int(input('n='))
    for i in range(1,n+1):
        i=int(input())
        L.append(i)
    return L

def tong(L):
    s=0
    j=0
    while j<len(L):
        if j%2!=0:
            s+=L[j]
        j+=1
    print(f'Tong={s}')
    
L=Input()
tong(L)