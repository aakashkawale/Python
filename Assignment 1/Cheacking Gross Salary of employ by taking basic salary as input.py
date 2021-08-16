bs=int(input("Enter Your Basic Salary : "))
if bs<=10000:
    hra=(bs*20)/100
    da=(bs*80)/100
    gs=bs+hra+da
    print("Your Gross Salary Is", gs)
elif bs>=10000 and bs<=20000:
    hra=(bs*25)/100
    da=(bs*90)/100
    gs=bs+hra+da
    print("Your Gross Salary Is", gs)
elif bs>20000:
    hra=(bs*30)/100
    da=(bs*95)/100
    gs=bs+hra+da
    print("Your Gross Salary Is", gs)