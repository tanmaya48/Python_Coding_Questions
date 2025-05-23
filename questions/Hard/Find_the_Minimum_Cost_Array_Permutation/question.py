from typing import List

def findPermutation(nums: List[int]) -> List[int]:
    """
    You are given an array `nums` which is a permutation of `[0, 1, 2, ..., n -
    1]`. The **score** of any permutation of `[0, 1, 2, ..., n - 1]` named `perm`
    is defined as:
    
    `score(perm) = |perm[0] - nums[perm[1]]| + |perm[1] - nums[perm[2]]| + ... +
    |perm[n - 1] - nums[perm[0]]|`
    
    Return the permutation `perm` which has the **minimum** possible score. If
    multiple permutations exist with this score, return the one that is
    lexicographically smallest among them.

    **Constraints:**
    
      * `2 <= n == nums.length <= 14`
      * `nums` is a permutation of `[0, 1, 2, ..., n - 1]`.
    """