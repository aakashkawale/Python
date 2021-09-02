class Node:
    def __init__(self):
        self.info = 0
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def insert(self, x):
        n1 = Node()
        n1.info = x

        if self.start==None:
            self.start = n1
        else:
            n1.next=self.start
            self.start = n1


    def remove(self):
        if self.start== None:
            print("Linked list is empty")
        else:
            print("deleted iteam ", self.start.info)
            self.start=self.start.next

    def show(self):
        temp=self.start
        while temp!=None:
            print(temp.info)
            temp=temp.next






ob = LinkedList()
ob.insert(10)
ob.insert(20)
ob.insert(30)
ob.insert(40)
ob.show()
print("===========================")
ob.remove()
ob.show()
