def LaSoNguyenTo(x):
    if x==2:
        return True
    for i in range(2,x):
        if x%i==0:
            return False
        else:
            u=True
    return u

def SoHopLe(x):
    if x<=1:
        return True
    else:
        return False

def NhapvaDem():
    kq=0
    print('Nhap day so:')
    while True:
        x=int(input())
        if SoHopLe(x)==True:
            break
        else:
            if LaSoNguyenTo(x)==True:
                kq+=1
    return kq
        
def InKQ(kq):
    print(f'Co {kq} so nguyen to')
    
kq=NhapvaDem()
InKQ(kq)