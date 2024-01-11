str=input('str=')
ch=input('ch=')

str=str.lower()
ch=ch.lower()

dem=0
for i in new_str:
    if i==ch:
        dem+=1
print(f'Number of character {ch} is: {dem}')
