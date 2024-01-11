def NhapSo(thongbao):
    print(thongbao)
    while True:
        x=input()
        if x.isnumeric():
            return int(x)
        else:
            print("Khong hop le!!!")

a=NhapSo("Nhap so nguyen a:")
b=NhapSo("Nhap so nguyen b:")
print("a+b=",a+b)