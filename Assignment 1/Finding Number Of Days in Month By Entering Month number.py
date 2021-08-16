a=int(input("Enter Your Month Number : "))
b=(1,3,5,7,8,10,12)
if a in b :
    print("Number Of Days Are 31")
elif a==2:
    print('Number Of Days are 28 or 29')
else:
    print('Number of days are 30')