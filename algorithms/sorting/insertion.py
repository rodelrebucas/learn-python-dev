"""
    TODO: Implement
    O(n^2), Best case O(n) - sorted, nearly sorted
    Insert the value in the right place in the sub array

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