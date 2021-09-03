class test:
    def __init__(self,x=0,y=0):
        self.i=x
        self.j=y
        print("init method with default args called")
    def addition (self):
        print(self.i+self.j)

t1=test()
t1.addition()
t2=test(30,40)
t2.addition()