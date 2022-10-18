class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class sLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

list = sLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("wed")

# Linked 1st node to 2nd node
list.headval.nextval = e2

# linked 2nd node to 3rd node
e2.nextval = e3

list.listprint()