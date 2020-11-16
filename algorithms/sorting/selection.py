"""
Selection Sort: O(n^2)

    Example:

    unsortedArr = [10, 2, 6, 1, 8]
    
    Pseudo Code:

        First Iteration:
        
            1. Set a starting minimum value:

                minIndex = 0
            
            2. Second iteration starting on current index + 1

                a. Second iteration starts at index 1 (0 + 1): [2, 6, 1, 8]
                b. Look for a value that is lesser than the current minIndex:

                    b.1 Assumed minimum value: 10 at index 1; unsortedArr[minIndex]
                    b.2 Current value of 2nd iteration: unsortedArr[1] < unsortedArr[minIndex]
                    b.3 Replace minIndex with current index: minIndex = current index (1)
                c. Iterate until length of unsortedArr
            
            3. Swap the values at the end of second iteration

                unsortedArr[minVal], unsortedArr[current index] = unsortedArr[current index], unsortedArr[minIndex]

"""


def selectionSort(data):
    for i in range(len(data)):
        ## Set a minimum value
        # set minimum index with the current iteration index
        min_index = i

        ## Find the minimum value
        # inner iteration for comparing each
        # element against the minimum element.
        for j in range(
            i + 1, len(data)
        ):  ## Do not include the starting element since it is the set minimum value
            #  so there's no need for comparison
            if data[j] < data[min_index]:  ## Ascending
                ## Get the index of the minimum element
                min_index = j

        ## Swap current index with the minimum index if it's not the minimum index
        if i != min_index:
            data[i], data[min_index] = data[min_index], data[i]

    return data


if __name__ == "__main__":

    data = [
        [3, 4, 6, 2, 3, 1, 1, 2, 2, 37, 0],
        [1, 2, 3, 4, 5],
        [2.4, 99, 2, 4, 1, 1, -1, 0, 0],
        [9, 8, 7, 6, 3, 2, 1],
    ]

    for i in range(len(data)):
        print(selectionSort(data[i]))
