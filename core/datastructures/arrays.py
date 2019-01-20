"""

Array a collection of items

Time complexity
    Remove last item  O(1)
    Remove middle item O(n)
    Insert O(n)
    Add O(1)
"""

array_l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(array_l1[0])  # 1

# iterations:

for i in array_l1:
    print(i)

for i in range(len(array_l1)):
    print(i)

# slicing

print(array_l1[:])  # print all contents
print(array_l1[::-1])  # prints reverse
print(array_l1[:-1])  # prints all except last item
print(array_l1[1:])  # prints all except first item
print(array_l1[::-2])  # prints reverse skipping every second item
print(array_l1[::2])  # prints all skipping every second item
print(array_l1[1:7])  # prints from second index (1) up to index 7-1
