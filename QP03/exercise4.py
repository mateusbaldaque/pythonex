n = int(input())
i = 0
if n % 2 == 0:
    while i < n:
        a = n / 2
        b = int(a - 1)
        if i == a or i == b:
            c = b * '#'
            print('{}00{}'.format(c,c))
        else:
            print(n*'#')
        i += 1
else:
    y=0
    while y < n:
        a1 = int(n // 2)
        if y == a1:
            d = a1 * '#'
            print('{}0{}'.format(d,d))
        else:
            print(n*'#')
        y += 1