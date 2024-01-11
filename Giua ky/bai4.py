n=int(input())
s=0
x=0
next_s=0
while s<=n:
    next_s=s+x
    if next_s >n:
        x=x-1
        break
    else:
        s+=x
        x+=1
print(x)