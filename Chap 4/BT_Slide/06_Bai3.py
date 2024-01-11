def ktr(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def songuyento(n):
    A=[]
    i=2
    while len(A)<n:
        if ktr(i):
            A.append(i)
        i+=1
    print(', '.join(map(str, A)))
    
def nhap():
    n=int(input("n="))
    return n

n=nhap()
ktr(n)
songuyento(n)