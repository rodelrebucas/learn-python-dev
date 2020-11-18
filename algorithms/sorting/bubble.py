"""
    Bubble sort

        Swap elements until its in the right place
        Sort ascending: [4, 3, 1, 2]

        Pseudo Code: (Ascending)
            1. Iterate array in reverse(outer), len(arr) - 1 = 4 iterations or 3 down to 0
                [4, 3, 1, 2] 
            2. Iterate array (inner) through outer iteration range, meaning iterations will be: 3, 2, 1, 0
                a. Compare current index with curent index + 1
                    If current index > curent index + 1; swap   
            1st iteration:
                [3, 1, 2, 4] - 4 is in place, inner iteration range is 3
            2nd iteration:
                [1, 2, 3, 4] - 3 is in place, inner iteration range is 2
                ...   
"""

import pytest


def bubbleSort(l):
    # outer iterations is len(l) - 1
    # inner iterations is up outer - 1
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):  # this makes sure j + 1 won't exceed with list's length
            # Swap
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


@pytest.fixture(
    params=[
        {"input": [3, 2, 1], "expected": [1, 2, 3]},
        {"input": [1, 2, 3, 4, 5], "expected": [1, 2, 3, 4, 5]},
        {"input": [3, 2, 1, 1, 2, 2, 2, 4], "expected": [1, 1, 2, 2, 2, 2, 3, 4]},
    ]
)
def testCase(request):
    return request.param


def test_bubblesort(testCase):
    assert bubbleSort(testCase["input"]) == testCase["expected"]
