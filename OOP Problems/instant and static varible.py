class test :
    def __init__(self,x):
        # instant
        self.i=x
        #static
        test.j=0
    def inr (self):
       test.j+=1
    def show(self):
        print(self.i,test.j)

t1=test(10)
t2=test(20)
t1.inr()
t2.inr()
t1.show()
t2.show()