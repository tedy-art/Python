print('This is Global scope')

x = 100
def outer_fun():
    print("We are in local scope of outer function.")

    def inner_fun():
        print("We are in local scope of inner function.")

        def super_inner():
            print("Super inner function in inner function.")
        
        print("We are calling super inner function in local scope")
        super_inner()
        return super_inner

    print("We are calling inner function from local scope of outer function")
    inner_fun()
    return inner_fun

print("we are calling outer function from global scope")
s = outer_fun()
print(type(s))