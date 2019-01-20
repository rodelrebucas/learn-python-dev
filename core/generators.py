"""

Generators  
    Functions that return iterators.
    __iter__, __next__() and StopIteration are implemented already
    Must contain atleast one yield statement

Yield
    Yield pauses the current state of the function, then
    continues for successive calls wherever it left of.

Iterators
    objects that we can iterate with

"""

# Examples


def simple_gen():
    yield "1. First Call"
    yield "2. Second Call"


def simple_gen_add(n):
    n = n + 1
    yield n

    n = n + 1
    yield n


def fib_gen():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    n = 0
    # iterator can only be iterated once
    simple_gen_iter = simple_gen()
    print(next(simple_gen_iter))  # 1. First Call
    print(next(simple_gen_iter))  # 2. Second Call
    # StopIteration traceback
    # print(next(simple_gen_iter))

    # variables are remembered
    simple_gen_add_iter = simple_gen_add(n)
    print(next(simple_gen_add_iter))
    print(next(simple_gen_add_iter))

    # creating new instance
    simple_gen_iter = simple_gen()

    # using loops to iterate
    for val in simple_gen_iter:
        print(val)

    # generator expression
    (i for i in range(100))
    num_iter = (i for i in range(100))

    print(next(num_iter))  # 0
    print(next(num_iter))  # 1

    print("FIB")
    # fibonnaci using generators
    fib_iter = fib_gen()
    for _ in range(6):
        print(next(fib_iter))
