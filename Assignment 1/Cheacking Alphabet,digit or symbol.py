ch = input("Enter Your Char : ")
if 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
    print("It is a alphabet")
elif 48 <= ord(ch) <= 57:
    print("It is a digit")
else:
    print("It is a symbol")
