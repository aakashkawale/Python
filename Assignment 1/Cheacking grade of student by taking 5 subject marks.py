p=int(input("Enter Your phyics marks : "))
c=int(input("Enter Your chemistry marks : "))
m=int(input("Enter Your maths marks : "))
b=int(input("Enter Your biology marks : "))
co=int(input("Enter Your computer marks : "))
per=(p+c+m+b+co)/5
print(per)
if per>=90:
    print("A")
elif per>=80 and per<=90:
    print("B")
elif per>=70 and per<=80:
    print("C")
elif per>=60 and per<=70:
    print("D")
elif per>=50 and per<=60:
    print("E")
elif  per <= 40:
    print("F")