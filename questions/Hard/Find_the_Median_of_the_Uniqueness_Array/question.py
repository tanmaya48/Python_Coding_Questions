from typing import List

def medianOfUniquenessArray(nums: List[int]) -> int:
    """
    You are given an integer array `nums`. The **uniqueness array** of `nums` is
    the sorted array that contains the number of distinct elements of all the
    subarrays of `nums`. In other words, it is a sorted array consisting of
    `distinct(nums[i..j])`, for all `0 <= i <= j < nums.length`.
    
    Here, `distinct(nums[i..j])` denotes the number of distinct elements in the
    subarray that starts at index `i` and ends at index `j`.
    
    Return the **median** of the **uniqueness array** of `nums`.
    
    **Note** that the **median** of an array is defined as the middle element of
    the array when it is sorted in non-decreasing order. If there are two choices
    for a median, the **smaller** of the two values is taken.
    
    **Constraints:**
    
      * `1 <= nums.length <= 10 ^ 5`
      * `1 <= nums[i] <= 10 ^ 5`
    """