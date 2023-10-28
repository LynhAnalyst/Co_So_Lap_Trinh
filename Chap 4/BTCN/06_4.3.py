from math import sqrt

def nhap():
    print('Nhap 3 so nguyen:')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c

def giaipt(a,b,c):
    d=b*b-4*a*c
    if d<0:
        x1=True
        x2=False
    elif d==0:
        x1=x2=-b/2*a
    else:
        x1=(-b+sqrt(d))/2*a
        x2=(-b-sqrt(d))/2*a
    return x1,x2

def inkq(x1,x2):
    if x1==True and x2==False:
        print(f'Phuong trinh vo nghiem')
    elif x1==x2:
        print(f'Phuong trinh co nghiem kep\nx1=x2={x1}')
    elif x1<x2 or x1>x2:
        print(f'Phuong trinh co hai nghiem\nx1={x1}\nx2={x2}')

a,b,c=nhap()
x1,x2=giaipt(a,b,c)
inkq(x1,x2)