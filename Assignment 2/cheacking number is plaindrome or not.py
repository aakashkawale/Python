a=int(input("Enter Your Number : "))
b=str(a)
c=b[::-1]
c=int(c)
if a==c:
    print('It is a plaindrome Number')
else:
    print('it is not a plaindrome number')