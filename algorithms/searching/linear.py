"""

    Time complexity O(n)

"""

# Search for maximum number
l = [2, 4, 5, 1, 80, 5, 99]

maximum = l[0]

for item in l:
    if item > maximum:
        maximum = item

print(maximum)
