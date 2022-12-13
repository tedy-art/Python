print("This is Global scope..")

def outer_func():
    print("This is local scope of outer function..")

    def inner_func():
        print("This is local scope of inner function..")

    inner_func()

print("We are calling outer function from global scope..")
outer_func()