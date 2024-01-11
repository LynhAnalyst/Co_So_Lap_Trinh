st1=input('st1=')
st2=input('st2=')
st3=input('st3=')

def checkstring(st1,st2,st3):
    if st1.startswith(st2) and st1.endswith(st3):
        return True
    else:
        return False

print(checkstring(st1,st2,st3))
    