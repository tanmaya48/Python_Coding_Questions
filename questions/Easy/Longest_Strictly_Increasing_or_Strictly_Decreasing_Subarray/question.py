from typing import List


INC = 0
DEC = 1
EQ = 2
def get_tone(n,m):
    if n < m:
        return INC
    elif n > m:
        return DEC
    return EQ

def longestMonotonicSubarray(nums: List[int]) -> int:
    """
    You are given an array of integers `nums`. Return the length of
    the **longest** subarray of `nums` which is either **strictly increasing** or
    **strictly decreasing**.
    **Constraints:**
      * `1 <= nums.length <= 50`
      * `1 <= nums[i] <= 50`
    """
    if len(nums) == 1:
        return 1
    longest = 0
    start=0
    while True:
        if start == len(nums) -1:
            break
        tone = get_tone(nums[start],nums[start+1])
        if tone == EQ:
            longest = max(longest,1)
            start+=1
            continue
        for i in range(start+1,len(nums)):
            if i == len(nums)-1:
                break
            if get_tone(nums[i],nums[i+1]) != tone:
                break
        length = (i - start) +1
        if length > longest:
            longest = length
        start = i 
    return longest



