n=int(input('n='))
gt=1

if n==1:
    print(f'{n}!=0')
elif 0<=n<=100:
    for i in range(1,n+1):
        gt*=i
print(f'{n}!={gt}')