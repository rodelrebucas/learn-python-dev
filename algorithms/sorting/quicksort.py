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