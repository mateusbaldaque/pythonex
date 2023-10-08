n1 = int(input())
n2 = int(input())

reversed_n1= 0
while n1 != 0:
    digit1 = n1 % 10
    digit2 = n2 % 10
    reversed_n1 = reversed_n1 * 100 + digit1 * 10 + digit2
    n1 //= 10
    n2 //= 10


print(reversed_n1)