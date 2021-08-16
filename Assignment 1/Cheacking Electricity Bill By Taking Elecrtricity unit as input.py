a=int(input("Enter Your Electricity Units : "))
if a<=50:
    b=a*0.50
    ac=(a*20)/100
    tb=b+ac
    print("Your Light Bil Is " + str(tb) + " Rs")
elif a>50 and a<=150:
    b=a*0.75
    ac=(a*20)/100
    tb=b+ac
    print("Your Light Bil Is " + str(tb) + " Rs")
elif a>150 and a<=250:
    b=a*1.20
    ac=(a*20)/100
    tb=b+ac
    print("Your Light Bil Is " + str(tb) + " Rs")
elif a>250:
    b=a*1.50
    ac=(a*20)/100
    tb=b+ac
    print("Your Light Bil Is " + str(tb) + " Rs")