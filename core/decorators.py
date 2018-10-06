'''
   Decorators - use to modify functions or classes
        Functions
            - 1st class objects
                meaning:
                    functions can be referenced by a variable
                    pass as argument and use as arguments
                    define inner functions
'''
# ------------------------------------->
# decorator function
def decorator_func(func):
    # inner function that modifies the func
    def wrapper():
        print("Wrapper started")
        # call the func
        func()
        print("Wrapper closed")
    
    return wrapper

# ------------------------------------->
# Inner wrapper that accepts any arguments

import functools
def decorator_func_two(func):
    # make sure func does not lose its identity.
    # func.__name__ prints correct func name not the wrapper's name
    @functools.wraps(func)
    # make sure the decorator can also accept any args passed to the decorated function
    def wrapper(*args, **kwargs): 
        print("Wrapper started")
        # call the func
        func(*args, **kwargs)
        print("Wrapper closed")

        # If you want to return the value
        # return func(*args, **kwargs) 
        
    return wrapper

# ------------------------------------->
# Decorating without wrapping

def register(func):
    registered_func[func.__name__] = func
    return func

# ------------------------------------->
# Decorator with arguments or without

def upper(_func=None, *, letters=None):
    #  - arguments are both optional
    #  - * syntax tell that/enforces all following args must be keyword - this is needed to achieve optional args
    
    #  1. if the decorator is called without arguments then decorated function is passed
    #   letters argument is None since the first argument must be the function being decorated,
    #   apply the decoration.

    #  2. if the decorator passes an argument (must only passed the set keyword argument) _func will be none and
    #  letters have value, so **return a function that will be used as the decorator**  
    def decorator_upper(func):
        @functools.wraps(func)
        def wrapper_upper(*args, **kwargs):
            wrapper_upper.a = 1
            value = func(*args, **kwargs)
            if letters:
                for l in letters:
                    value = value.replace(l, l.upper())
            else:
                return value.upper()
            return func(*args, **kwargs)
        wrapper_upper.a = 1
        return wrapper_upper
    
    # With arguments
    if _func is None:
        print(letters)
        print('FUNC: ', _func)
        return decorator_upper
    # Without arguments
    else:
        print(letters)
        print('FUNC: ', _func)
        return decorator_upper(_func)          

if __name__ == "__main__":

    # ------------------------------------->
    # create a function to be decorated
    def function_one():
        print("function_one")
    decorated_function = decorator_func(function_one)
    decorated_function()

    # shorter syntax
    # create a function to be decorated
    @decorator_func
    def function_two():
        print("function_two")

    function_two()

    # ------------------------------------->
    # Inner wrapper that accepts any arguments
    @decorator_func_two
    # create a function to be decorated
    def function_three(any_args):
        print(f"function three has {any_args}")

    # test any parameters
    function_three("name")
    function_three(1)
    function_three([1,2,3])

    # ------------------------------------->
    # Decorating without wrapping
    registered_func = dict()
    @register
    def member_one():
        print("Register me!")
    
    member_one()
    print(registered_func) # Register me!
    registered_func['member_one']() # Register me!


    # ------------------------------------->
    # Decorator with arguments
    # Pass a letter to be uppercased
    # if params empty uppercase all
    @upper(letters='re')
    def enter_name(name):
        return name 
    
    print(enter_name('rodel')) # RodEl
    
    @upper
    def enter_name(name):
        return name 
    
    print(enter_name('ryan')) # RODEL

    d = enter_name('cheslit')
    print(d.a)