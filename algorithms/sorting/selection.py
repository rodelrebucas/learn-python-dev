"""

Selection Sort

    1. Set minimum value
    2. Search all elements for minimum value by comparing the set minimum value
    3. Swap the current minimum value with newly found minimum value

    Pseudo Code:
        
        list iteration:
            minimum_value = first_iter_current_list_index

            second_iteration:
                minimum_value < second_iter_current_list_index
                    minimum_value = second_iter_current_list_index
             
            swap places
                current index value  = minimum index value
                minimum index value = current index value

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

        ## If minimum value is already in placed
        # there is no need to swap
        # meaning , current index is the minimum element
        if i != min_index:
            ## Swap current index with the minimum index
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
