db='$#@'
str=input()
kq=False
while 6<=len(str)<=17:
    if any(i for i in str if i in db): 
        if any(i for i in str if i.isupper()):
            if any(i for i in str if i.isalpha()):
                kq=True
                break
    else:
        break

print(kq)