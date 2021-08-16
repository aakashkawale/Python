a = input('Enter Your String : ')
b=[]
c=[]
for i in a:
   b.append(i)
for j in b:
    d=b.count(j)
    c.append(d)
for l in c:
    if d > 1:
        print('Deja Hu')
    else:
        print('Umiqe')