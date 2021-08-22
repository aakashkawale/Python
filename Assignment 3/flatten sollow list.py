o = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
s=[]
for i in range(0,len(o)):
    a=o[i]
    for x in a:
        ab = s.append(x)
print(s)