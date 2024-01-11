def nhap():
    a=float(input('a='))
    b=float(input('b='))
    tt=input('Toan tu: ')
    return a,b,tt

def kq(a,b,tt):
    if tt=='+':
        print(f'{a}+{b}={a+b}')
    if tt=='-':
        print(f'{a}-{b}={a-b}')
    if tt=='*':
        print(f'{a}*{b}={a*b}')
    if tt=='/':
        if b==0:
            print(False)
        else:
            print(f'{a}+{b}={a+b}')
            
def laplai():
    while True:
        ll=input('Tiep tuc: ')
        if ll=='T' or ll=='t':
            break
        else:
            nhap()
            kq(a,b,tt)      
        
a,b,tt=nhap()
kq(a,b,tt)
laplai()