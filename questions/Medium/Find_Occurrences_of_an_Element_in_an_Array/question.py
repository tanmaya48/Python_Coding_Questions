from typing import List

def occurrencesOfElement(nums: List[int], queries: List[int], x: int) -> List[int]:
    """
    You are given an integer array `nums`, an integer array `queries`, and an
    integer `x`.
    For each `queries[i]`, you need to find the index of the `queries[i]th`
    occurrence of `x` in the `nums` array. If there are fewer than `queries[i]`
    occurrences of `x`, the answer should be -1 for that query.
    Return an integer array `answer` containing the answers to all queries.
    **Constraints:**
      * `1 <= nums.length, queries.length <= 10 ^ 5`
      * `1 <= queries[i] <= 10 ^ 5`
      * `1 <= nums[i], x <= 10 ^ 4`
    """
    occurances = [i for i,c in enumerate(nums) if c == x]
    indexes = [occurances[q-1] if q <= len(occurances) else (-1) for q in queries]
    return indexes
    
