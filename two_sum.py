def two_sum_pairs(numbers, target):
    """
    Return all value pairs as sets such that the two values sum to the target.

    The pairs are returned in the order discovered by a simple nested for-loop:
    - Outer loop goes i from 0..len(numbers)-1
    - Inner loop goes j from i+1..len(numbers)-1

    This problem is intentionally specified to support beginner-friendly
    implementations using lists, for-loops, and append but also to practice our DM Concepts into Programming.

    Examples:
        numbers = [1, 2, 3, 4], target = 5 -> [{1, 4}, {2, 3}]
        numbers = [3, -1, 4, -3, 5], target = 2 -> [{3, -1}, {-3, 5}]

    Args:
        numbers: List of integers (can include duplicates and negatives).
        target: Integer target sum.

    Returns:
        A list of sets containing the two values that sum to the target.
    """
    # TODO A list of sets containing the two values that sum to the target.
