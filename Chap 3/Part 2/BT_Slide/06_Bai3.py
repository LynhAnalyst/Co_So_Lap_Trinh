n=int(input('n='))

while 0<=n<=9999:
    if 0<=n<10:
        print(f'{n} co 1 chu so')
    elif 10<=n<100:
        print(f'{n} co 2 chu so')
    elif 100<=n<1000:
        print(f'{n} co 3 chu so')
    else:
        print(f'{n} co 4 chu so')
    break