import pytest

from two_sum import two_sum_pairs


def test_empty_list_returns_empty():
    result = two_sum_pairs([], 10)
    assert result == [], f"Expected [] (empty list) but got {result}. An empty list should return an empty list."


def test_single_element_returns_empty():
    result = two_sum_pairs([7], 7)
    assert result == [], f"Expected [] (empty list) but got {result}. A single element cannot form a pair."


def test_no_pairs_found():
    result = two_sum_pairs([1, 2, 4], 100)
    assert result == [], f"Expected [] (empty list) but got {result}. No pairs in [1, 2, 4] sum to 100."


def test_basic_pairs_order_by_discovery():
    result = two_sum_pairs([1, 2, 3, 4], 5)
    expected = [{1, 4}, {2, 3}]
    assert result == expected, f"Expected {expected} but got {result}. In [1, 2, 3, 4], the pairs that sum to 5 are 1+4 and 2+3."




def test_mixed_numbers_and_negatives():
    numbers = [3, -1, 4, -3, 5]
    target = 2
    result = two_sum_pairs(numbers, target)
    expected = [{3, -1}, {-3, 5}]
    assert result == expected, f"Expected {expected} but got {result}. In [3, -1, 4, -3, 5], the pairs that sum to 2 are 3+(-1) and (-3)+5."




def test_same_value_non_adjacent_indices():
    result = two_sum_pairs([5, 1, 5], 10)
    expected = [{5}]
    assert result == expected, f"Expected {expected} but got {result}. Note: When you have duplicate values like [5, 1, 5], you should only return one set {5}, not multiple sets."


def test_large_target_and_order_stability():
    nums = [1, 9, 8, 2, 7, 3, 6, 4, 5]
    target = 10
    result = two_sum_pairs(nums, target)
    expected = [{1, 9}, {8, 2}, {3, 7}, {4, 6}]
    assert result == expected, f"Expected {expected} but got {result}. Check that you're finding all pairs that sum to {target} and not including duplicates."


def test_return_value_pairs_as_sets():
    pairs = two_sum_pairs([1, 4, 2, 3], 5)
    expected = [{1, 4}, {2, 3}]
    assert pairs == expected, f"Expected {expected} but got {pairs}. Make sure you're returning sets, not lists or tuples."
    assert all(isinstance(p, set) and len(p) <= 2 for p in pairs), "Each pair should be a set with at most 2 elements."
    assert all(isinstance(i, int) for p in pairs for i in p), "All values in the sets should be integers."
