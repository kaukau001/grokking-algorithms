import pytest
from src.chapter1.binary_search import binary_search


@pytest.mark.parametrize("ordered_list, item, expected_index", [
    ([1, 3, 5, 7, 9, 11, 13], 7, 3),  # Test when the element is found
    ([1, 3, 5, 7, 9, 11, 13], 8, None),  # Test when the element is not found
    ([], 5, None),  # Test with an empty list
    ([5], 5, 0),  # Test with a single element list
    ([1, 3, 5, 7, 9], 3, 1),  # Test with an odd-length list
    ([1, 3, 5, 7, 9, 11], 7, 3)  # Test with an even-length list
])
def test_binary_search(ordered_list, item, expected_index):
    assert binary_search(ordered_list, item) == expected_index
