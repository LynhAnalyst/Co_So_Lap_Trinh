n=int(input())
tong=0
if 0<=n<=10000:
    for i in str(n):
        tong+=int(i)
    if str(tong)[-1]=='9':
        print('YES')
    else:
        print('NO')