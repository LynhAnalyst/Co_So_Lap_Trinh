L=[]
def nhap():
    a=1
    while a<=10:
        n=int(input())
        L.append(n)
        a+=1
    return L

def ktr(L):
    x=int(input('x='))
    for i in (L):
        if i==5:
            i=x
    print(L)
            
L=nhap()
ktr(L)