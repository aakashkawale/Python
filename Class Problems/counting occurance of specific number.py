a=input("Enter Your String : ")
b=input("Enter the word you want to find count")
if b in a :
    x=a.count(b)
    print(x)
else:
    print(f"{b} not in String")