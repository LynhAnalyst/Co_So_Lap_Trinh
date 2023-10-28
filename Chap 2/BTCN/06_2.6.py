ten = input('Ho ten: ')
so_ngay_cong = int(input('So ngay cong: '))
don_gia = int(input('Don gia ngay cong: '))
he_so = float(input('He so phu cap: '))
tam_ung = int(input('Tam ung: '))

luong = don_gia*so_ngay_cong*he_so
thuc_linh = luong-tam_ung

print(f'Nhan vien {ten}, Co tien Luong={round(luong,1)}, Tam ung={tam_ung} va Thuc linh={round(thuc_linh,1)}')