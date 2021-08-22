s=[1,2,3,2,3,4,3]
a= ' '.join([str(elem) for elem in s])
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
