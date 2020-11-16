"""
    Quicksort - sorting by dividing and conquer.
    Time complexity O(Nlog2^N)

    Pseudo-code:
        1. Choose a pivot - a value to be consider as a basis for comparison of lower and higher.
            pivot = len(array) - 1
        2. Move values lower than the pivot at the lower part of the array and move values
           greaterthan the pivot at higher part of the array.
           ....Details (wip)
        3. Place the pivot at the correct place when no unsorted values for lower and higher exist.
           Logically it should be after the lower part and before the higher part,
           since: lower values <= pivot =< higher values
"""

# import pytest

# @pytest.fixture(
#     params=[
#         {"input": [8, 9, 8, 9, 1, 2, 0, 1], "expected": [0, 1, 1, 2, 8, 8, 9, 9]},
#         {"input": [9, 7, 6, 4, 5], "expected": [4, 5, 6, 7, 9]},
#         {"input": [6, 5, 3, 1, 4, 2, 7, 10], "expected": [1, 2, 3, 4, 5, 6, 7, 10]},
#     ]
# )
# def testcase(request):
#     return request.param


# def test_quicksort(testcase):
#     assert (
#         quicksort(testcase["input"], 0, len(testcase["input"]) - 1)
#         == testcase["expected"]
#     )