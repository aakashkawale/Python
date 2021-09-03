class test:
    def __init__(self,x,y):
        self.i=x
        self.j=y
        print("init method with args called")
    def addition (self):
        print(self.i+self.j)

t1=test(10,20)
t1.addition()
t2=test(30,40)
t2.addition()