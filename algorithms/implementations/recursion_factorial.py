"""

    A factorial implementation using recursion

    n = 5
    Iterations:
        5 * (factorial(4)) [n-1] -> return 120 [5 * 4 * 3 * 2 * 1]
            4 * (factorial(3)) -> return 4
                3 * (factorial(2)) -> return 3
                    2 * factorial(1) -> return 2
                        n == 1
                            -> return 1
    
    Calls function over and over until a return value is found

"""


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))
