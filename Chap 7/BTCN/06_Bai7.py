str=input().split(', ')
email=[]
for i in str:
    if '@' in i:
        email=i
        break
for j in email:
    print(email[7:])
    break
