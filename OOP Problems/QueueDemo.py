class Queue:

    def __init__(self):
        self.rear = -1
        self.front = 0
        self.arr = []
        self.max = 5

    def insert(self, x):
        if self.rear == self.max - 1:
            print("Queue is full")
        else:
            self.rear += 1
            self.arr.insert(self.rear, x)
            print("Inserted item", x)

    def remove(self):
        if self.rear < self.front:
            print("Queue is empty")
        else:
            print("Delete item is ", self.arr[self.front])
            self.front += 1

    def show(self):
        for i in range(self.front, self.rear + 1):
            print(self.arr[i])


ob = Queue()
ob.insert(10)
ob.insert(20)
ob.insert(30)
ob.insert(40)
ob.insert(50)
ob.insert(60)
print("==================")
ob.show()
ob.remove()
print("==================")
ob.show()