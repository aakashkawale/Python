n = int(input("Enter your number : "))
for x in range(100, n + 1):
    a = x
    i = 0
    c=len(str(x))

    while a > 0:
        b = a % 10
        i = i + b ** c
        a = a // 10
    if x == i:
        print(i)
