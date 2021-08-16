a = int(input("Enter your number : "))

b = [int(x) for x in str(a)]
c = len(b)
d = b[0]
b[0] = b[c - 1]
b[c - 1] = d
for i in b:
    print(i, end='')
