while True:
    a=float(input('a='))
    b=float(input('b='))
    toan_tu=input('Toan tu:')

    if toan_tu=='+':
        kq=a+b
    elif toan_tu=='-':
        kq=a-b
    elif toan_tu=='/':
        kq=a/b
    elif toan_tu=='*':
        kq=int(a*b)

    print(f'{a}{toan_tu}{b}={kq}')
    
    tiep_tuc=input('Tiep tuc:')
    if tiep_tuc == 't' or tiep_tuc =='T':
        break
    
