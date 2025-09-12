def two_sum_pairs(numbers, target):
    """
    Return all index pairs (i, j) such that i < j and numbers[i] + numbers[j] == target.

    The pairs are returned in the order discovered by a simple nested for-loop:
    - Outer loop goes i from 0..len(numbers)-1
    - Inner loop goes j from i+1..len(numbers)-1

    This function is intentionally specified to support beginner-friendly
    implementations using lists, for-loops, and append.

    Examples:
        numbers = [1, 2, 3, 4], target = 5 -> [(0, 3), (1, 2)]
        numbers = [2, 2, 2], target = 4 -> [(0, 1), (0, 2), (1, 2)]

    Args:
        numbers: List of integers (can include duplicates and negatives).
        target: Integer target sum.

    Returns:
        A list of tuples of indices (i, j) with i < j.
    """
    raise NotImplementedError("Implement using nested for-loops and list append")
