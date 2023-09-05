def cache_function_result(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    
    return wrapper


@cache_function_result
def expensive_operation(x):
    print(f"expensive opearation for {x}")
    return x * x


print(expensive_operation(9))
print(expensive_operation(9))
print(expensive_operation(7))
print(expensive_operation(7))