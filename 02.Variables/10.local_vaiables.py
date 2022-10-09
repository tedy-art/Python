#if you create a variable with the same name inside a function, this variable will be
# local, & can only be used inside the function the global variable with the same name
# will remain as it was, global & with the original value.

x = "awesome"

def myFunc():
    x = "funtastic"
    print("Python is "+x)

myFunc()
print("Python is "+x)