# a Single Node of a singly linked List
class Node:
    # Constructor
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next


# A linked list class with a sigle head node
class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion method for a linkedlist
    def insert(self,data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method for linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

# Singly linked list with insertion and print
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()