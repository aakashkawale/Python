s=int(input('Enter your Selling Price : '))
c=int(input("Enter Your Cost Price :  "))
a=s-c
if a>0:
    print("You Made A Profit Of "+str(a)+" Rs")
elif a<0:
    print("You Made A Loss Of "+str(a)+" Rs")

