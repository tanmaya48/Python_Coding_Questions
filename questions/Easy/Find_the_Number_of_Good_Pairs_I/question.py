from typing import List

def numberOfPairs(nums1: List[int], nums2: List[int], k: int) -> int:
    """
    You are given 2 integer arrays `nums1` and `nums2` of lengths `n` and `m`
    respectively. You are also given a **positive** integer `k`.
    
    A pair `(i, j)` is called **good** if `nums1[i]` is divisible by `nums2[j] *
    k` (`0 <= i <= n - 1`, `0 <= j <= m - 1`).
    
    Return the total number of **good** pairs.

    
    **Constraints:**
    
      * `1 <= n, m <= 50`
      * `1 <= nums1[i], nums2[j] <= 50`
      * `1 <= k <= 50`
    """
    knums2 = [k*val for val in nums2]
    success = 0
    for i in nums1:
        for j in knums2:
            if i%j == 0:
                success+=1
    return success
