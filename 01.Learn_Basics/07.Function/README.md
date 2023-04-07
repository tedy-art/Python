FUNCTION:
    A function is a block of code which is only runs when it is called.
    you can pass data, known as parameter, into function.
    A function can return data as a result.

Basic sysntax for defining a Function in python:
    def function_name(parameter):
        #statement(s)
        retrun expressions
To call this function syntax:-
    function_name()

Arguments in pythn function:
    while definig a function in python, you can pass argument(s) into the function by
    putting them inside the parenthesis.

syntax:
    def function_name(arg1, arg2):
        #what to do with function
When the function is called, then you need to specify a value for the arguments
syntax:
    function_name(arg1, arg2)

How to use the return keyword in python:
    In python, you can use the keyword return to exit a function so it goes back to
    where it was called. That is send something out of the function.

The return statement can contain an expression to execute once the function is called.

Arbitary argument, *args:
    If you do not know hoe many arguments that will be passed into your function, add
    a "*" before the parameter name in the function definition.
Syntax:
    def functionName(*args):
        #statement(s)

    functionName(argValue1,argValue2,argValue3,.....argValueN)