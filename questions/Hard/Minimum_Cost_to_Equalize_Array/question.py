from typing import List

def minCostToEqualizeArray(nums: List[int], cost1: int, cost2: int) -> int:
    """
    You are given an integer array `nums` and two integers `cost1` and `cost2`.
    You are allowed to perform **either** of the following operations **any**
    number of times:
    
      * Choose an index `i` from `nums` and **increase** `nums[i]` by `1` for a cost of `cost1`.
      * Choose two **different** indices `i`, `j`, from `nums` and **increase** `nums[i]` and `nums[j]` by `1` for a cost of `cost2`.
    
    Return the **minimum** **cost** required to make all elements in the array
    **equal**.
    
    Since the answer may be very large, return it **modulo** `10 ^ 9 + 7`.
    
    **Constraints:**
    
      * `1 <= nums.length <= 10 ^ 5`
      * `1 <= nums[i] <= 10 ^ 6`
      * `1 <= cost1 <= 10 ^ 6`
      * `1 <= cost2 <= 10 ^ 6`
    """