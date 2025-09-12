import pytest

from two_sum import two_sum_pairs


def test_empty_list_returns_empty():
    assert two_sum_pairs([], 10) == []


def test_single_element_returns_empty():
    assert two_sum_pairs([7], 7) == []


def test_no_pairs_found():
    assert two_sum_pairs([1, 2, 4], 100) == []


def test_basic_pairs_order_by_discovery():
    # Outer i increases left-to-right; inner j checks to the right of i
    # Expected discovery order for [1,2,3,4], target 5:
    # (0,3)->1+4, then (1,2)->2+3
    assert two_sum_pairs([1, 2, 3, 4], 5) == [(0, 3), (1, 2)]


def test_duplicates_generate_multiple_pairs():
    # For [2,2,2], target 4, the pairs are (0,1), (0,2), (1,2)
    assert two_sum_pairs([2, 2, 2], 4) == [(0, 1), (0, 2), (1, 2)]


def test_mixed_numbers_and_negatives():
    numbers = [3, -1, 4, -3, 5]
    target = 2
    # Pairs by discovery:
    # i=0: j=1(3+-1=2)->(0,1), j=2(3+4=7), j=3(3+-3=0), j=4(3+5=8)
    # i=1: j=2(-1+4=3), j=3(-1+-3=-4), j=4(-1+5=4)
    # i=2: j=3(4+-3=1), j=4(4+5=9)
    # i=3: j=4(-3+5=2)->(3,4)
    assert two_sum_pairs(numbers, target) == [(0, 1), (3, 4)]


def test_zero_and_zero_pairs():
    assert two_sum_pairs([0, 0, 0], 0) == [(0, 1), (0, 2), (1, 2)]


def test_same_value_non_adjacent_indices():
    # Ensure indices (not values) are returned and in correct order
    assert two_sum_pairs([5, 1, 5], 10) == [(0, 2)]


def test_large_target_and_order_stability():
    # Ensure order matches i<j nested loops
    nums = [1, 9, 8, 2, 7, 3, 6, 4, 5]
    target = 10
    expected = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                expected.append((i, j))

    assert two_sum_pairs(nums, target) == expected


def test_do_not_return_value_pairs_only_index_pairs():
    # Guardrail: ensure students return index pairs (tuples of ints)
    pairs = two_sum_pairs([1, 4, 2, 3], 5)
    assert pairs == [(0, 1), (2, 3)]
    assert all(isinstance(p, tuple) and len(p) == 2 for p in pairs)
    assert all(isinstance(i, int) for p in pairs for i in p)
