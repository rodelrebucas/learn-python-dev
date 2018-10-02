'''
   Decorators - use to modify functions or classes
        Functions
            - 1st class objects
                meaning:
                    functions can be referenced by a variable
                    pass as argument and use as arguments
                    define inner functions
'''
# decorator function
def decorator_func(func):
    # inner function that modifies the func
    def wrapper():
        print("Wrapper started")
        # call the func
        func()
        print("Wrapper closed")
    
    return wrapper

# create a function to be decorated
def function_one():
    print("function_one")


# ------------------------------------->


import functools

def decorator_func_two(func):
    # make sure func does not lose its identity.
    # func.__name__ prints corrent func name not the wrapper's name
    @functools.wraps(func)
    # make sure the decorator can also accept any args passed to the decorated function
    def wrapper(*args, **kwargs): 
        print("Wrapper started")
        # call the func
        func(*args, **kwargs)
        print("Wrapper closed")
    
    return wrapper

# ------------------------------------->


if __name__ == "__main__":
    decorated_function = decorator_func(function_one)
    decorated_function()

    # shorter syntax
    # create a function to be decorated
    @decorator_func
    def function_two():
        print("function_two")

    function_two()


    @decorator_func_two
    # create a function to be decorated
    def function_three(any_args):
        print(f"function three has {any_args}")
    
    # test any parameters
    function_three("name")
    function_three(1)
    function_three([1,2,3])