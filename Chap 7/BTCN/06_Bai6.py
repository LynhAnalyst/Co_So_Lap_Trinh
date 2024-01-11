L=input().split(',')
kq=[]
for i in L:
    a=int(i,2)
    if a%3==0:
        kq.append(i)    
if kq:
    print(','.join(kq))
else:
    None