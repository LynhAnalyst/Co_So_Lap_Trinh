A=[]
B=[]
for i in range(1,11):
    x=int(input())
    A.append(x)
B=A
for i in range(0,len(A),2):
    B[i],B[i+1]=A[i+1],A[i]
    
for j in B:
    print(j, end=' ')