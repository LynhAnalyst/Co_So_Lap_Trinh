x=float(input('x='))
y=float(input('y='))
ch=input('Phep toan:')

if ch=='+':
    kq=x+y
    print(f'{x}{ch}{y}={round(kq,1)}')
elif ch=='-':
    kq=x-y
    print(f'{x}{ch}{y}={round(kq,1)}')
elif ch=='*':
    kq=x*y
    print(f'{x}{ch}{y}={round(kq,1)}')
elif ch=='/':
    if y==0:
        print('Khong hop le')
    else:
        kq=x/y
        print(f'{x}{ch}{y}={round(kq,1)}')
else:
    print('Khong hop le')