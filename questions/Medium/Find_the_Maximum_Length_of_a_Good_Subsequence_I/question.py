from typing import List

def maximumLength(nums: List[int], k: int) -> int:
    """
    You are given an integer array `nums` and a **non-negative** integer `k`. A
    sequence of integers `seq` is called **good** if there are **at most** `k`
    indices `i` in the range `[0, seq.length - 2]` such that `seq[i] != seq[i +
    1]`.
    Return the **maximum** possible length of a **good** subsequence of `nums`.    
    **Constraints:**
      * `1 <= nums.length <= 500`
      * `1 <= nums[i] <= 10 ^ 9`
      * `0 <= k <= min(nums.length, 25)`
    """
    max_seq_len = 1
    for start in range(len(nums)-1):
        ks = 0
        seq_len =1
        for end in range(start+1,len(nums)):
            if nums[end-1] != nums[end]:
                ks+=1
            if ks > k:
                break
            seq_len+=1



