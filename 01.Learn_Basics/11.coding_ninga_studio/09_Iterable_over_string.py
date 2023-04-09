# def iterate(s):
#     # Write your code here.
#     for i in s:
#         print(i)
# s = input()
# iterate(s)

def iterator(s):
    itr = iter(s)
    size = len(s)
    while size>0:
        print(next(itr))
        size = size-1

user_input = input()
iterator(user_input)