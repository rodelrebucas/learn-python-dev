# select pivot
# partition - items lesser that pivot on the left and greater on the right
# sort left and right elements
# recurse


def partition(l, low, high):
    # select pivot
    pivotIndex = l[high]

    # position where to do a next swap
    # swap index and swapIndex's value
    swapIndex = low
    for index in range(low, high):
        if l[index] < l[high]:
            l[swapIndex], l[index] = l[index], l[swapIndex]
            swapIndex = swapIndex + 1

        index = index + 1

    # swap the last index  and the swap index's value
    l[swapIndex], l[high] = l[high], l[swapIndex]

    return swapIndex


def quicksort(l, low, high):
    if low < high:
        pivot = partition(l, low, high)
        quicksort(l, low, pivot - 1)  # left part
        quicksort(l, pivot + 1, high)  # right part
    return l


lt = [8, 9, 8, 9, 1, 2, 0, 1]
# lt = [9, 7, 6, 4, 5]
# lt = [6, 5, 3, 1, 4, 2, 7, 10]
print(quicksort(lt, 0, len(lt) - 1))
