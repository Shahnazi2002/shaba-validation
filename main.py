number = input("لطفا شماره شبا را بدون IR و بدون فاصله وارد کنید: ")
if len(number) == 24:
    number += "1827"
    number += number[:2]
    integer = int(number[2:])
    r = integer % 97
    if r == 1:
        print("شماره شبا صحیح است")
    else:
        print("شماره شبا وارد شده معتبر نیست")
else:
    print("شماره شبا به صورت صحیح وارد نشده است")