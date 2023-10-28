import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

S=(a+b+c)/2
dien_tich=math.sqrt(S*(S-a)*(S-b)*(S-c))

print(f'Dien tich={float(dien_tich)}')
