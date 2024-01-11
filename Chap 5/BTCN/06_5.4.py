def Input():
    A=[]
    n=int(input('n='))
    for i in range(1,n+1):
        i=int(input())
        A.append(i)
    return A

def daonguoc(A):
    B=[]
    A.reverse()
    B=A
    print(B)
    return B
    
def sapxep(B):
    B.sort()
    print(B)
    
A=Input()
B=daonguoc(A)
sapxep(B)