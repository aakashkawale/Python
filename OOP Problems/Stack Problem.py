class stack:
    def __init__(self):
        self.top = -1
        self.arr = []
        self.max = 5

    def push(self, x):
        if self.top == self.max-1:
            print("Stack is overflow..")
        else:
            self.top += 1
            self.arr.insert(self.top,x)
            print(x, "Pushed at..", self.top)

    def pop(self):
        if self.top == -1 :
            print("Stack is underflow...")
        else:
            print("popped iteam is..", self.arr[self.top])
            self.top-=1

    def show(self):
        if self.top == -1:
            print("Stack is empty..")
        else:
            print("Stack iteam are..")
            for i in range (self.top, -1, -1):
                print(self.arr[i])

a = stack()
a.push(10)
a.push(20)
a.push(30)
a.push(40)
a.push(50)
a.push(60)
a.show()
a.pop()
a.pop()
a.show()
