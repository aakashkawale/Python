a=str(input("Enter Your String : "))
a=a.split(" ")
b=len(a)
for i in range(0, b) :
    c=a[i]
    x=a.count(c)
    i+=1
    print(f"count of {c} is {x}")
