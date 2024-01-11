def Input():
    L=[]
    n=int(input('n='))
    for i in range(1,n+1):
        i=int(input())
        L.append(i)
    return L

def songuyen(L):
    s=0
    for i in L:
        if i>0:
            s+=1
    print(f'SND={s}')

def tbc(L):
    s=0
    m=0
    for i in L:
        if i%2==0:
            m+=i
            s+=1
    if s==0:
        print(f'TBC=0')
    else:
        print(f'TBC={float(m/s)}')  

L=Input()
songuyen(L)
tbc(L)