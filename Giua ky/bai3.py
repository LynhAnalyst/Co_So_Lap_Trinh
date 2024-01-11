a=int(input())
b=int(input())
c=int(input())

def tinh_a(a,b,c):
    if a<=100:
        tien_a=(15*b)+(20*c)
    if a>100:
        tien_a=((a-100)*25)+(15*b)+(20*c)
    print(tien_a)
    
def tinh_b(a,b,c):
    if a<=250:
        tien_b=(35*b)+(25*c)
    if a>250:
        tien_b=(45*(a-250))+(35*b)+(25*c)
    print(tien_b)

tinh_a(a,b,c)
tinh_b(a,b,c)