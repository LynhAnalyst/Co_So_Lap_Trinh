while True:
    mk=input()
    if len(mk)<8 or mk.isnumeric() or mk.isalpha() or mk.isupper() or mk.islower(): 
       print('Khong hop le') 
    else:
        print('Hop le')
        break