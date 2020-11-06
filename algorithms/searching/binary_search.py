
# Time complexity - log2N or O(log(n)) - (It is assume that it's base 2)
# For every length of N of array
# the number of times to search for the item is log2N
# E.g length 16 = log2N = log2 (4) + 1 since we need to compare the single item remaining in worst case scenerio
def binarySearch(arr, searchVal):
    minv = 0
    maxv = len(arr) - 1
    while(maxv >= minv):
        # We start guessing at the middle of the array. 
        guess = int((minv + maxv)/ 2)
        if (arr[guess] == searchVal):
            print("Found")
            return
        # Guess lower
        # We need to move at the lower part of the array
        # and discard  part of the array that starts at index maxv - 1
        if (arr[guess] > searchVal):
            maxv = guess - 1
        # Guess higher
        # We need to move at the higher part of the array
        # and discard  part of the array that starts at index minv + 1
        if (arr[guess] < searchVal):
            minv = guess + 1
    print("Not found") 
    return
    
if __name__ == "__main__":
    s = 1
    arr = [1,2,3,4,5,6,7,8,10,12,34,67,11]
    binarySearch(arr, s)
