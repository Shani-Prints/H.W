import time

#ex_1
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@timing_decorator
def time_func(num):
    for i in range(num):
        j=0


time_func(90000000)

#ex_2
def cache_decorator(func):
    cache={ }
    def wrapper(*args,**kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            print("Returning cached result")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

@timing_decorator
@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
