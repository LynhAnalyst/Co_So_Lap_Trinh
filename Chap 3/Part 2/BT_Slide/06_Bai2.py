n=int(input('n='))
x=0

if n==2:
    x=1
elif 2<n<=100:
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:
            x=1

if x==1:
    print(f'{n} la SNT')
else:
    print(f'{n} khong la SNT')
        