L=[]
while True:
    n=int(input())
    if n==0:
        break
    L.append(n)
    
L.reverse()
for i in L:
    print(i)