"""
TODO: Implement

Merge Sort - sorting by recursively dividing the array into sub arrays, sorting out into the right place then merging back again.

Time complexity: O(nLog2^N): n is the time to merge N size array, Log2^N + 1 is the no. of time an N size of array can be divided.

Pseudo Code:
    1. Determine the middle of the array:
        m = len(arr) / 2
    2. Recursively divide the lower part indices 0 - m and upper part m + 1 to len(arr) - 1
    3. Take note an array that contains a single element is consider sorted, the only step to do is merge it on the right place.
"""