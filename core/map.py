"""
    Map
        - expects a function
        - also expects any no. of iterables (list, dictionary, ...)
        - then executes the function for each item in the iterable 
"""


def multiply_two(num):
    return num * 2


print(list(map(multiply_two, [1, 2, 3])))  # [2, 4, 6]

# Using lambda
result = list(map(lambda x: x * 2, [1, 2, 3]))
print(result)  # [2, 4, 6]

# two iterables
result = list(map(lambda x, y: x * y, [1, 2, 3], [2, 4, 6]))
print(result)  # [2, 8, 18]
