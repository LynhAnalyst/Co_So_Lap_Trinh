niem_yet = int(input('Nhap Gia niem yet: '))
chiet_khau = int(input('Nhap Chiet khau: '))

VAT = (niem_yet-chiet_khau)*0.01
gia_ban = niem_yet-chiet_khau+VAT

print(f'Gia ban: {float(gia_ban)}')