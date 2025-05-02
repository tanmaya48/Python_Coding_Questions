from typing import List


def get_bitwise_or_sum(sub_array):
    bit_vals = [32,16,8,4,2,1]
    bits_sum = 0
    remaining_array = sub_array
    for bit_val in bit_vals:
        has_bits = [1 for val in remaining_array if val >= bit_val]
        if sum(has_bits) >= 1:
            bits_sum+=bit_val
        remaining_array = [val if val < bit_val else val-bit_val for val in remaining_array]
    return bits_sum
    

def minimumSubarrayLength(nums: List[int], k: int) -> int:
    """
    You are given an array `nums` of **non-negative** integers and an integer `k`.
    An array is called **special** if the bitwise `OR` of all of its elements is
    **at least** `k`.
    Return the length of the**shortest** **special** **non-empty** subarray of
    `nums`, or return `-1` if no special subarray exists.
    **Constraints:**
      * `1 <= nums.length <= 50`
      * `0 <= nums[i] <= 50`
      * `0 <= k < 64`
    """
    values = nums
    min_size = 100
    for start in range(len(nums)):
        for size in range(1,len(nums)+1-start):
            sub_array = nums[start:start+size]
            if get_bitwise_or_sum(sub_array) >= k:
                if size < min_size:
                    min_size = size
    if min_size < 100:
        return min_size
    return -1
    
