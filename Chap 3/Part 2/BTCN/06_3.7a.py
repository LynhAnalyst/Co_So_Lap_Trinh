while True:
    n=int(input())
    a=1
    if n<0:
        break
    while n>=1:
        a*=n
        n-=1
    print(a)