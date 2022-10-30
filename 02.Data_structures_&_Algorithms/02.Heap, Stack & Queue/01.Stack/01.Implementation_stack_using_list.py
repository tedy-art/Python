"""
Python program to demonstrate stack implementation using list
"""
stack = []

# append() function to push elements in stack
stack.append('a')
stack.append('b')
stack.append('c')

print("Initial stack:")
print(stack)

# pop() function to pop elements from stack in LIFO order.
print("\nElements popped from stack : ")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nstack after elements are popped : ')
print(stack)


"""
uncommenting "print(stack.pop())" will cause an error an IndexError as the stack is 
now empty
"""