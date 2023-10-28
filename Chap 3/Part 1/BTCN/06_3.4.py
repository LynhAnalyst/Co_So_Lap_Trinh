toan=int(input())
ly=int(input())
hoa=int(input())

trung_binh=(toan*2+ly*3+hoa)/6

if trung_binh <3:
    print('Kem')
elif 3<=trung_binh<5:
    print('Yeu')
elif 5<=trung_binh<6:
    print('Trung binh')
elif 6<=trung_binh<7:
    print('Trung binh Kha')
elif 7<=trung_binh<8:
    print('Kha')
elif 8<=trung_binh<9:
    print('Gioi')
elif 9<=trung_binh<10:
    print('Xuat sac')