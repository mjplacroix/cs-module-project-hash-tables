cache = {}
def fib(n):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    
    return cache[n]

for i in range(1000):
    print(f'{i:3} {fib(i)}')


# def fib(n):
#     if n <= 1:
#         return n

#     return fib(n-1) + fib(n-2)

# for i in range(50):
#     print(f'{i:3} {fib(i)}')