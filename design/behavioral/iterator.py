from __future__ import print_function

# generator function
def count_to(count):
    for i in range(1, count + 1):
        yield i


count_to_five = count_to(5)

# by iteration
for count in count_to_five:
    print(count)

# Create new instance
count_to_five = count_to(5)
# by next()
try:
    while True:
        print(next(count_to_five))
except StopIteration as e:
    print("Iteration Done...")
