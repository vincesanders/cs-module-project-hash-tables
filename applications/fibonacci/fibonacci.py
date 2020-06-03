# def fib(n): # O(2^n)
#     if n <= 1:
#         return n
    
#     return fib(n - 1) + fib(n - 2)

cache = {}

def fib(n): # O(n)
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

for i in range(100):
    print(f'{i:3} {fib(i)}')