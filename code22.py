def execution_time(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function finished")
        return result

    return wrapper


@execution_time
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"Factorial={result}")
    return result


factorial(5)