from functools import reduce

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Use map() to generate squares of all numbers
squares = list(map(lambda x: x**2, number))

# 2. Use filter() to extract even numbers
evens = list(filter(lambda x: x % 2 == 0, number))

# 3. Use reduce() to calculate sum of all numbers
total = reduce(lambda acc, x: acc + x, number)

print("1. Squares:", squares)
print("2. Even numbers:", evens)
print("3. Sum of all numbers:", total)