"""
    Filter
        - expects a function
        - expects only ONE iterable
        - returns the filtered result based on the condition set on the function

"""

# return True if x is divisble by 3 otherwise false
div_three = lambda x: x % 3 == 0

result = list(filter(div_three, [1, 2, 3, 0, 6, 8, 9, 18]))
print(result)  # [3, 0, 6, 9, 18]
