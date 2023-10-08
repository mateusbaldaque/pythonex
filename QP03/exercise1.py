n = int(input())
i = 1
a = 1
if n == 0:
    while a <= 10:
        res3 = a * n
        print(n, "x", a, '=', res3 )
        a += 1
else:
    while i < n and i <= 10:
        res = i * n
        print(n, "x", i, '=', res )
        if n == i:
            res2 = n ** 2
            print(n, '^ 2 =', res2)
        i += 1

    
