a = int(input("enter 3 digit number : \n"))
b = a // 100

c = a % 100

d = c // 10

e = c % 10

f = (b ** 3) + (d ** 3) + (e ** 3)

if a==f:
    print('It IS Armstrong Number')
else:
    print('It Is Not Armstrong Number')
