class test:
    def __init__(self):
        self.i=10
        self.j=20
        print("init method without args called")
    def addition (self):
        print(self.i+self.j)
t1=test()
t1.addition()
t2=test()
t2.addition()
