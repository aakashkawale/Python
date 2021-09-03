class test:
    k = 0

    def __init__(self, x, y):
        self.i = x
        self.j = y
        self.__class__.k += 1

    def sqr(self):
        self.i *= self.i
        self.j *= self.j

    def show(self):
        print(self.i, self.j, self.__class__.k)

t1=test(3,4)
t2=test(5,6)

t1.sqr()
t2.sqr()
t1.show()
t2.show()
