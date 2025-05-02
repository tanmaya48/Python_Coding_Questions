from typing import List

def duplicateNumbersXOR(nums: List[int]) -> int:
    """
    You are given an array `nums`, where each number in the array appears
    **either** once or twice.
    
    Return the bitwise `XOR` of all the numbers that appear twice in the array,
    or 0 if no number appears twice.
    
    **Constraints:**
    
      * `1 <= nums.length <= 50`
      * `1 <= nums[i] <= 50`
      * Each number in `nums` appears either once or twice.
    """
    twice_nums = []
    for i in range(len(nums)):
        if nums[i] in nums[i+1:]:
            twice_nums.append(nums[i])
    if len(twice_nums) == 0:
        return 0
    bits_sum  = 0
    remaining_nums = twice_nums
    for num in [32,16,8,4,2,1]:
        has_bit = [1 for n in remaining_nums if n >= num ]
        if sum(has_bit)%2 == 1:
            bits_sum += num
        remaining_nums = [val-num if val >= num else val for val in remaining_nums]
    return bits_sum

