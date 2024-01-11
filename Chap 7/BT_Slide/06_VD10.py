# Nhập từ bàn phím 2 chuỗi ký tự st1 và st2.
# Cho biết st2 xuất hiện bao nhiêu lần trong st1 (không phân biệt chữ hoa và chữ thường.

st1="banana"
st2="na"

st1=input("st1: ").lower()
st2=input("st2: ").lower()
dem=0
i=0
while True:
    i=st1.find(st2,i)
    if i>=0:      
        print("Vi tri:",i)
        dem=dem+1
        i=i+1
    else:
        break
   
print("So lan xuat hien:",dem)