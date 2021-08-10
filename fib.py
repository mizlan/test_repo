def fib(n):
    if n < 0:
        raise ValueError
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(6))
