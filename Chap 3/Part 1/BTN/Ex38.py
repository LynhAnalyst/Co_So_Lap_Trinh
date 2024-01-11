month=(int(input('Thang:')))

if month in (1,3,5,7,8,10,12):
    print(f'Thang {month} co 31 ngay')
elif month in (4,6,9,11):
    print(f'Thang {month} co 30 ngay')
elif month==2:
    year=int(input('Nam:'))
    if (year%4==0 and year%100==0) or (year%400==0):
        print(f'Thang 2 co 29 ngay')
    else:
        print(f'Thang 2 co 28 ngay')