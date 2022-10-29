# single node of singly linked list
class Node:
    # Constructor
    def __init__(self,data=None, next = None):
        self.data = data
        self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

#Linked List with a single node
LL = LinkedList()
LL.head = Node(3)
print(LL.head.data)