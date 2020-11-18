"""
    Quicksort - sorting by dividing and conquer.
    Time complexity:
        Best case: O(Nlog2^N), pivot is the median
        Worst Case: O(n^2), pivot is either always the highest or lowest part

    Pseudo-code: array = [5, 2, 4, 6, 8, 3]
        1. Partitioning:
            a. Choose a pivot - a value to be considered as a basis for comparison which leads to a partitioned
                array of lower part and higher part.
                
                * pivot = len(array) - 1

            b. Move values lower than the pivot at the lower part of the array and move values
               greater than the pivot at higher part of the array.
                    i = swap_index - 1
                    j = iteration_index 
                    

                    Iterations: 
                        i = 0
                        j = 0 (* j (1) can start higher than i since if j and i is equal there is no need to swap )
                        j <= 3(pivot); false;


                        i = 0
                        j = 1
                        j <= 3(pivot); true; increment_swap index; swap
                        [2,5,4,6,8,3]

                        i = 1
                        j = 2
                        j <= 3(pivot); false;

                        i = 1
                        j = 3,4 (j does not reach the higher part index)
                        j <= 3(pivot); false;
                    
                   * Swap the pivot with latest swap index value the end of iterations.
                        Why? Logically it should be after the lower part and before the higher part,
                        since: lower values >= pivot < higher values

                    i = 1 + 1
                    pivot = 3 at index 5
                    [2,3,4,6,8,5]

            c. Now all values at left of the pivot are <= pivot and right part are > pivot.
               Proceed to first partition and recursion.

                * Return the current swap_index(1) as the new pivot 

        
        2.Recurse the array while lower index < higher index (lower index > higherindex denotes that it is already out of bounds so we stop),
            with current resulting indexes:
                lower part: lower_index, pivot - 1; [2]
                higher part: pivot + 1, higher_index; [4,5,8,5]
"""
import pytest


def partition(arr, low, high):
    # Choose a pivot
    pivot = arr[high]

    # Start the swap index outside the current array just below the first element
    swap_index = low - 1

    # Iterate current array until index < high
    for index in range(low, high):

        # For every value that is lesser than the pivot:
        # 1. Increment swap_index
        # 2. Make a swap.
        # Incrementing the swap index before swapping makes sure
        # that we are swapping at the right place.
        if arr[index] < pivot:
            swap_index = swap_index + 1
            arr[swap_index], arr[index] = arr[index], arr[swap_index]

    # Final swapping to make sure that the left of the pivot is lesser and
    # at the right, values greater than the pivot.
    swap_index = swap_index + 1
    arr[high], arr[swap_index] = arr[swap_index], arr[high]

    # This is the new pivot
    return swap_index


def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)
    return arr


@pytest.fixture(
    params=[
        {"input": [8, 9, 8, 9, 1, 2, 0, 1], "expected": [0, 1, 1, 2, 8, 8, 9, 9]},
        {"input": [9, 7, 6, 4, 5], "expected": [4, 5, 6, 7, 9]},
        {"input": [6, 5, 3, 1, 4, 2, 7, 10], "expected": [1, 2, 3, 4, 5, 6, 7, 10]},
    ]
)
def testcase(request):
    return request.param


def test_quicksort(testcase):
    assert (
        quicksort(testcase["input"], 0, len(testcase["input"]) - 1)
        == testcase["expected"]
    )