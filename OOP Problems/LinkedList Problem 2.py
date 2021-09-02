class Node:
    def __init__(self):
        self.info = 0
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def insert(self, x):
      n1=Node()
      n1.info=x
      n1.next=n1
    # def remove(self):
    #    n1.next=
    def show(self):
        pass

ob = LinkedList()
ob.insert(10)
ob.insert(20)
ob.insert(30)
ob.insert(40)
ob.show()
print("===========================")
ob.remove()
ob.show()
