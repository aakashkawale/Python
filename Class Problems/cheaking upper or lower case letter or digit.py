ch = input("enter char : ")
a = ord(ch)
if a >= 65 and a <= 90:
    print("Capital")
elif a >= 97 and a <= 122:
    print("small")
elif a >= 48 and a <= 57:
    print('Digit')
