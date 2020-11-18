# Time complexity - log2N or O(log(n)) - (It is assume that it's base 2)
# For every length of N of array
# the number of times to search for the item is log2^N
# E.g length 16 = log2^N = log2 (4) + 1 since we need to compare the single item remaining in worst case scenerio
def binarySearch(arr, searchVal):
    minv = 0
    maxv = len(arr) - 1
    # maxv < minv; search index has reach -1 index or greater than array size
    while maxv >= minv:
        # We always guess at the middle of the array.
        guess = int((minv + maxv) / 2)
        if arr[guess] == searchVal:
            print("Found")
            return
        # Guess lower
        # We need to move at the lower part of the array
        # and discard  part of the array that is greater index maxv - 1
        if arr[guess] > searchVal:
            maxv = guess - 1
        # Guess higher
        # We need to move at the higher part of the array
        # and discard  part of the array that is less than index minv + 1
        if arr[guess] < searchVal:
            minv = guess + 1
    print("Not found")
    return


if __name__ == "__main__":
    s = 3
    # Sorted array
    arr = [1, 2, 3, 4, 5]
    binarySearch(arr, s)
