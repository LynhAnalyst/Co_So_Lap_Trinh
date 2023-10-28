duong=0
am=0

while True:
    n=int(input())
    if n>0:
        duong+=1
    elif n<0:
        am+=1
    if n==0:
        break

print(f'{duong} so duong')
print(f'{am} so am')