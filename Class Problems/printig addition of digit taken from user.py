a=int (input(" Enter your number : "))
i=0
while a>0 :
    b=a%10
    i=b+i
    a=a//10
print(i)