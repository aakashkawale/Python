a=str(input("Enter Your String : "))
a=a.split(" ")
d1 = dict()
for i in range(0,len(a) ) :
    c=a[i]
    x=a.count(c)
    i+=1
    key=c
    value=x
    d1[key]=value

print(d1)
