'''
    Lambda or anonymous functions
        - can have any no. of arguments
        - only one expression
        - returns a function object
'''

# function
def multiply_to_two(num)
    return num * 2

print(multiply_to_two(2))

# lambda
mul = lambda x, y ; return x * y
print(mul(2))

map(mul, [1,2,3,4,5])