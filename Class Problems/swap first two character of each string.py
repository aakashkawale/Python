a=input("Enter your string")
b=input("Enter your string")


mylist=[]
for i in range(0,2):
    a=a.replace(a[i],b[i])
    b = b.replace(b[i], a[i])
    i += 1


mylist.append(a)
mylist.append(b)


print(mylist)
# s1=" ".join(mylist)
# print(s1)