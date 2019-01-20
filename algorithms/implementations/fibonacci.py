"""

Fibonnaci, a sequence of numbers resulted in adding
the previous number by the current number.

Starts with 0 and 1

0 + 1 = 1

fibonnaci sequence: 0 1 1 2 3 ...

"""


def fibonacci(n):
    a = 0
    b = 1
    for count in range(n):
        print(a)
        a, b = b, a + b


if __name__ == "__main__":
    # print the 1st 5 numbers of the sequence
    fibonacci(5)
