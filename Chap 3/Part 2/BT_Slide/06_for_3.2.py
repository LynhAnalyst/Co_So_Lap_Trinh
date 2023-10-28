n=int(input('n='))

if 1<=n<=50:
    for i in range(1,n+1):
        print(i,end=' ')
        if i%10==0:
            print()