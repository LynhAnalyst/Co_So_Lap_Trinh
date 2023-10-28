def Nhap():
    n=int(input('n='))
    return n

def NhapVaDem(n):
    kq=0
    print(f'Nhap {n} so nguyen:')
    for i in range(1,n+1):
        x=int(input())
        if x%2==0:
            kq+=1
    return kq

def InKQ(kq):
    print(f'So chu so chan la: {kq}')
        
n=Nhap()
kq=NhapVaDem(n)
InKQ(kq)