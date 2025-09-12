# two-sum-pairs-starter

Beginner Python exercise repo focused on lists, for-loops, and append using the two-sum (pairs that add to T) problem.

## Learning goals
- Loop over lists with elements and indices
- Build results with append
- Reason about duplicates and order
- Read test failures and fix code

## Function under test

Signature to implement in `two_sum.py`:

```python
def two_sum_pairs(numbers, target):
    """
    Return all index pairs (i, j) such that i < j and numbers[i] + numbers[j] == target.

    Use nested for-loops and append to collect results.
    Discovery order: for i in range(len(numbers)): for j in range(i+1, len(numbers)).
    """
    ...
```

## Quickstart
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
pytest
```

## Run command
Use the helper script to run tests consistently.
```bash
./run_tests.sh
```
