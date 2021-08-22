o = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
a=set()
for i in o:
    if type(i)==list:
        a.add("yes")

if "yes" in a:
    print("it contain sublist")
else:
    print("it doesn't contain sublist")