def fibonacciNumber(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1 or n == 2:
        return 1
    else:
        fib_prev = 1
        fib_curr = 1
        for i in range(3, n+1):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next
        return fib_curr

user_in = int(input())
# find the 10th Fibonacci number
print(fibonacciNumber(user_in))  # output: 55
