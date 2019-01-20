"""
    Lambda or anonymous functions
        - can have any no. of arguments
        - only one expression
        - returns a function object
"""

# function
def multiply_to_two(num):
    return num * 2


print(multiply_to_two(2))  # 4

# lambda
mul = lambda x, y: x * y
print(mul(2, 4))  # 8
