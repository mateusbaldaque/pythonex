h = int(input())
m = int(input())
if h>=24 or m >=60:
    print('INVALID DATE FORMAT')
else:
    if h < 12:
        if h == 0 and m == 0:
            print('12 am')
        else:
            if m < 10:
                print('{}:0{} am'.format(h,m))
            else:
                print('{}:{} am'.format(h,m))
    elif h >= 12:
        if h == 12 and m == 0 :
            print('12 pm')
        else:
            h = h - 12
            if m < 10:
                print('{}:0{} pm'.format(h,m))
            else:
                print('{}:{} pm'.format(h,m))






