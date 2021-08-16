a=int(input("Enter Your Number : "))

b=a//100
c=a%100
d=c//10
e=c%10
f= (b**3)+(d**3)+(e**3)
if a==f :
    print("It is armstrong number")
else:
    print("It is not armstrong number ")
