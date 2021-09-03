class test:
    count=0
    def __init__(self):
        test.count+=1

t1=test()
t2=test()
t3=test()
print('Numbers of object created ', test.count)