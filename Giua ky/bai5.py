a=int(input())
b=int(input())
s=0

A=[]

for i in range(a+1,b):
    if i%3==0:
        A.append(i)
        s+=1

if s>0:
    A.sort(reverse=True)
    for j in A:
        print(j,end=' ')
    
else:
    print('NOT FOUND')