import pytest

from two_sum import two_sum_pairs


def test_empty_list_returns_empty():
    assert two_sum_pairs([], 10) == []


def test_single_element_returns_empty():
    assert two_sum_pairs([7], 7) == []


def test_no_pairs_found():
    assert two_sum_pairs([1, 2, 4], 100) == []


def test_basic_pairs_order_by_discovery():
    assert two_sum_pairs([1, 2, 3, 4], 5) == [{1, 4}, {2, 3}]




def test_mixed_numbers_and_negatives():
    numbers = [3, -1, 4, -3, 5]
    target = 2
    assert two_sum_pairs(numbers, target) == [{3, -1}, {-3, 5}]




def test_same_value_non_adjacent_indices():
    assert two_sum_pairs([5, 1, 5], 10) == [{5}]


def test_large_target_and_order_stability():
    nums = [1, 9, 8, 2, 7, 3, 6, 4, 5]
    target = 10
    expected = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                expected.append({nums[i], nums[j]})

    assert two_sum_pairs(nums, target) == expected


def test_return_value_pairs_as_sets():
    pairs = two_sum_pairs([1, 4, 2, 3], 5)
    assert pairs == [{1, 4}, {2, 3}]
    assert all(isinstance(p, set) and len(p) <= 2 for p in pairs)
    assert all(isinstance(i, int) for p in pairs for i in p)
