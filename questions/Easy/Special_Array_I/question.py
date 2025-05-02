from typing import List


def isArraySpecial(nums: List[int]) -> bool:
    """
    An array is considered **special** if every pair of its adjacent elements
    contains two numbers with different parity.
    You are given an array of integers `nums`. Return `true` if `nums` is a
    **special** array, otherwise, return `false`.
    **Constraints:**
      * `1 <= nums.length <= 100`
      * `1 <= nums[i] <= 100`
    """
    for i in range(len(nums)-1):
        if (nums[i] - nums[i+1])%2 == 0:
            return False
    return True
