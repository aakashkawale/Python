a=int(input("Enter Your Number : "))
i=2
while i<a:
    if a%i==0:
        print('It Is Not Prime Number')
        break
    i+=1
if i==a:
    print("Prime Number")