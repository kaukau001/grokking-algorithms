import pytest
from src.chapter2.selection_sort import SelectionSort


@pytest.mark.parametrize("input_array, expected_output", [
    (["Naruto", "Luffy", "Goku", "Ichigo", "Saitama"],
     ["Goku", "Ichigo", "Luffy", "Naruto", "Saitama"]),  # Test sorting strings list
    ([], []),  # Test with an empty list
    ([21], [21]),  # Test with a single element list
    ([3, 2, 1], [1, 2, 3]),  # Test with a desc sorted list
    ([1, 2, 3], [1, 2, 3]),  # Test with an asc sorted list
])
def test_selection_sort_asc(input_array, expected_output):
    sorter = SelectionSort(input_array.copy())
    sorted_array = sorter.sort_asc()
    assert sorted_array == expected_output


@pytest.mark.parametrize("input_array, expected_output", [
    (["Naruto", "Luffy", "Goku", "Ichigo", "Saitama"],
     ["Saitama", "Naruto", "Luffy", "Ichigo", "Goku"]),  # Test sorting strings list
    ([], []),  # Test with an empty list
    ([13], [13]),  # Test with a single element list
    ([3, 2, 1], [3, 2, 1]),  # Test with a desc sorted list
    ([1, 2, 3], [3, 2, 1]),  # Test with an asc sorted list
])
def test_selection_sort_desc(input_array, expected_output):
    sorter = SelectionSort(input_array.copy())
    sorted_array = sorter.sort_desc()
    assert sorted_array == expected_output
