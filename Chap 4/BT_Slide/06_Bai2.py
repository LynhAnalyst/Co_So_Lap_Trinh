def nhap():
    n=int(input('n='))
    return n

def ktr(n):
    snt=True
    for i in range(2,n):
        if n%i==0:
            snt=False
            break
    return snt

def kq(snt):
    if snt==True:
        print(f'{n} la SNT')
    else:
        print(f'{n} khong la SNT')
                
n=nhap()
snt=ktr(n)
kq(snt)