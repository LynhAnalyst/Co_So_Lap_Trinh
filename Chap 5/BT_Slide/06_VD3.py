L=[]
while True:
    st=input()
    if st=='':
        break
    elif st not in (L):
        L.append(st)
print(L)