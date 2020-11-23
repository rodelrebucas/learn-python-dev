"""
    O(n^2), Best case O(n) - sorted, nearly sorted
    E.g [3,1,7,2,6]
    Pseudo code:
    1. Create sub array at index 0 which is [3], assumed to be sorted.
    2. Insert at the right place (ascending) values 1, 7, 2, 6 in to sub array.
        a. while unsorted subarray len is not 0
            b.iterate unsorted subarrays:
                b.1 While sorted subarray's current index < unsorted subarray's current index && sorted subarray's current index > -1
                b.2 Move sorted subarray's current index until exhausted.
                b.3 Insert unsorted array value at sorted subarray's current index + 1
                    1st insertion at index 0: [1, 3] - [7, 2, 6]
                    2nd insertion [1, 3, 7] - (7 is already in the right place), - [2, 6]
                    3rd insertion [1, 2, 3, 7], [6]
                    4th insertion [1, 2, 3, 6, 7]
                b.4 Shift sorted subarray values starting at current index + 1
"""

# Insertion by using sub-array and slicing
def insertionSort1(arr):
    sorted_arr = [arr[0]]
    for index in range(1, len(arr)):
        sorted_index = len(sorted_arr) - 1
        while arr[index] < sorted_arr[sorted_index] and sorted_index >= 0:
            sorted_index = sorted_index - 1

        # insert first
        if sorted_index < 0:
            sorted_arr = [arr[index]] + sorted_arr[sorted_index + 1 :]
        # insert in the middle or last
        # E.g: insert [2] in [1, 3, 7], sorted_index = 0
        else:
            sorted_arr = (
                sorted_arr[: sorted_index + 1]  # [1]
                + [arr[index]]  # [2]
                + sorted_arr[sorted_index + 1 :]  # [3, 7]
            )
            # [1, 2, 3, 7]
    return sorted_arr


# Insertion by moving elements
def insertionSort2(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        # key unsorted value
        key = arr[i]

        # Starting index of sorted values
        # E.g. [3, 1, 7, 2, 6]: index 0 is j
        # i - 1 since i started at 1 and increments
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position.
        # E.g. [3, 1, 7, 2, 6] , key=1 is lesser than 3
        # so move 3 up: [3, 3, 1, 7, 2, 6]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # We swap the key at the right place on sorted space
        # E.g. j = 0 + 1 and key = 1
        # [3, 3, 7, 2, 6]
        # [1, 3, 7, 2, 6]

        # What happens if key > arr[j]?
        # Ans: It is still swapped since:
        # arr[j + 1] = 7 and key = 7 when i = 2
        arr[j + 1] = key

        # Some Iterations:
        # key = 1 at index 1, index j = 0
        # [3, 3, 7, 2, 6]
        # [1, 3, 7, 2, 6]

        # key = 7 at index 2, index j = 1, key = 7, j + 1 is equal to 7
        # [1, 3, 7, 2, 6]
        # [1, 3, 7, 2, 6]

        # key = 2 at index 3, index j = 2,  [1, 3, 7, 2, 6]
        # 1st: [1, 3, 7, 7, 6]
        # 2nd: [1, 3, 3, 7, 6]
        # 3rd: j = 0, put key at j + 1: [1, 2, 3, 7, 6]

        # ...


arr = [3, 1, 7, 2, 6, 2, 1, 2, 10]
arr1 = insertionSort1(arr)

arr = [3, 1, 7, 2, 6]
insertionSort2(arr)

print(arr1, arr)