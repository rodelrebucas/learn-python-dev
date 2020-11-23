"""
TODO: Implement

Merge Sort - sorting by recursively dividing the array into sub arrays, sorting out into the right place then merging back again.

Time complexity: O(nLog2^N): n is the time to merge N size array, Log2^N + 1 is the no. of time an N size of array can be divided.

Pseudo Code:
    1. Determine the middle of the array:
        m = len(arr) / 2
    2. Split: Recursively divide the lower part indices 0 - m and upper part m + 1 to len(arr) - 1
    3. Merge: Take note an array that contains a single element is consider sorted, the only step to do is merge it on the right place.
"""


[6, 1, 9, 2, 8, 5, 4, 2]


[6, 1, 9, 2]

[6, 1] [9, 2]

[6] [1] [9, 2]


merge: [6] [1] -> [1 ,6]
merge: [9] [2] -> [2, 9]
merge: 
    [1, 6]
    [2, 9]

[1, 2, 6, 9]


[8, 9, 10]
[1, 2, 3]

[1, ]