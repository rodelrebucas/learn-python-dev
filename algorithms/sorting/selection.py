"""

selection.py







"""

data = [9, 1, 8, 6, 5, 2]
small = data[0]
small_index = 0
for i in range(len(data)):
    for j in range(len(data)):
        if data[j] < small:
            small_index = j
    print(small_index)
    data.pop(data[small_index])


