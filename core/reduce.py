"""
    Reduce
        - expects a function
        - expects only ONE iterable
        - return only one value
        - accumulates all the values in the iterable based on the operators set in the function
"""

from functools import reduce

l = [2, 3, 5, 5, 5]
total = lambda x, y: x + y
result = reduce(total, l)

print(result)  # 20
