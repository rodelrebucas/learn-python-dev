
# Time complexity - log2N
# For every length of N of array
# the number of times to search for the item is log2N
# E.g length 16 = log2N = log2 (4) + 1 since we need to compare the single item remaining in worst case scenerio
def binarySearch(arr, searchVal):
    minv = 0
    maxv = len(arr) - 1
    while(maxv >= minv):
        guess = int((minv + maxv)/ 2)
        if (arr[guess] == searchVal):
            print("Found")
            return
        # Guess lower
        if (arr[guess] > searchVal):
            maxv = guess - 1
        # Guess higher
        if (arr[guess] < searchVal):
            minv = guess + 1
    print("Not found") 
    return
    
if __name__ == "__main__":
    s = 1
    arr = [1,2,3,4,5,6,7,8,10,12,34,67,11]
    binarySearch(arr, s)
