def nhap():
    n=int(input('n='))
    return n

def ktr(n):
    for i in range(1,n+1):
        for j in range(1,i):
            if i%j==0:
                False
            else:
                print(j,end=' ',sep=', ')
                
n=nhap()
ktr(n)