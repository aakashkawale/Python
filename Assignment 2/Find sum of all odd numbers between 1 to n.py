n = int(input("Enter the number : "))
i = 1
c = 0

while i <= n:
    if i % 2 != 0:
        c = c + i

    i += 1
print(c)
