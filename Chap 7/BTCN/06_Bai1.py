str=input()
hoa=0
thuong=0
so=0
khac=0
for i in str:
    if i.isupper():
        hoa+=1
    if i.islower():
        thuong+=1
    if i.isdigit():
        so+=1
    else:
        khac+=1
        
print(f'In hoa: {hoa}')
print(f'In thuong: {thuong}')
print(f'Chu so: {so}')
print(f'Khac: {khac}')