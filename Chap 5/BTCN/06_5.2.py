def Input():
    L=[]
    n=int(input('n='))
    for i in range(1,n+1):
        i=int(input())
        L.append(i)
    return L

def Search(L):
    max=L[0]
    min=L[0]
    for j in L:
        if j>max:
            max=j
        if j<min:
            min=j
    return max,min

def Output(max,min):
    print(f'{max} {min}')

L=Input()
max,min=Search(L)
Output(max,min)