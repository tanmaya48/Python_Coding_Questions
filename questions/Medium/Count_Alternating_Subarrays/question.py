from typing import List

def is_alt(subarray):
    evens =subarray[::2] 
    odds =subarray[1::2] 
    if len(evens) == sum(evens) and sum(odds) == 0:
        return True
    if len(odds) == sum(odds) and sum(evens) == 0:
        return True
    return False

def countAlternatingSubarrays(nums: List[int]) -> int:
    """
    You are given a binary array `nums`.
    We call a subarray **alternating** if **no** two **adjacent** elements in the
    subarray have the **same** value.
    Return the number of alternating subarrays in `nums`.
    **Constraints:**
      * `1 <= nums.length <= 10 ^ 5`
      * `nums[i]` is either `0` or `1`.
    """
    subcount = 0
    for i in range(len(nums)):
        for size in range(1,len(nums)-i+1):
            if not is_alt(nums[i:i+size]):
                break
            subcount+=1
    return subcount


