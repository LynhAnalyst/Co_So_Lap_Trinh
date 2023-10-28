n=int(input('n='))

if 1<=n<=50:
    i=1
    while i<=n:
        print(i,end=' ')
        if i%10==0:
            print('')
        i+=1
