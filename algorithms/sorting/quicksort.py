import pytest

# select pivot
# partition - items lesser that pivot on the left and greater on the right
# sort left and right elements
# recurse


def partition(l, low, high):
    # select pivot
    pivotIndex = l[high]

    # position where to do a next swap
    # swap index and swapIndex's value
    swapIndex = low
    for index in range(low, high):
        if l[index] < l[high]:
            l[swapIndex], l[index] = l[index], l[swapIndex]
            swapIndex = swapIndex + 1

        index = index + 1

    # swap the last index  and the swap index's value
    l[swapIndex], l[high] = l[high], l[swapIndex]

    return swapIndex


def quicksort(l, low, high):
    if low < high:
        pivot = partition(l, low, high)
        quicksort(l, low, pivot - 1)  # left part
        quicksort(l, pivot + 1, high)  # right part
    return l


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

