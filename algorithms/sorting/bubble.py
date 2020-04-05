"""
Bubble sort

    Swap elements until its in the right place
    Sort ascending: [3, 2, 1]
    a. 1st iteration
        [2, 3, 1]
        [2, 1, 3]
    b. 2nd iteration: [2, 1, 3]
        [1, 2, 3]
"""

import pytest

xfail = pytest.mark.xfail


def bubbleSort(l):
    # outer iterations is len(l) - 1
    # e.g [5,4,3,2,1] = 1, 2, 3, 4 = iterations
    # this makes sure j + 1 won't exceed with list's length
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
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

