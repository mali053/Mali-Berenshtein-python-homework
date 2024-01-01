from datetime import datetime


def my_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


@my_decorator
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(15))
