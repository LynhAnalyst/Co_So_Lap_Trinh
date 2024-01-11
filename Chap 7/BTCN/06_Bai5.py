L=input().split()
n=int(input())
kq=False

for i in range(len(L)):
    if int(L[i])==n:
        kq=True
        print(i+1)
if not kq:
    print(0)