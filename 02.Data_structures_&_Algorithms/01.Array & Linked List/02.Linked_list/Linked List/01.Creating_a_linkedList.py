# Start with single linked list
# A single node of a singly linked list
# Creating a Node
class Node:
  # Constructor
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

# Creating a single node
first = Node(3)
print(first.data)