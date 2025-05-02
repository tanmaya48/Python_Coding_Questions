from typing import List

def mostFrequentIDs(nums: List[int], freq: List[int]) -> List[int]:
    """
    The problem involves tracking the frequency of IDs in a collection that
    changes over time. You have two integer arrays, `nums` and `freq`, of equal
    length `n`. Each element in `nums` represents an ID, and the corresponding
    element in `freq` indicates how many times that ID should be added to or
    removed from the collection at each step.
    
      * **Addition of IDs:** If `freq[i]` is positive, it means `freq[i]` IDs with the value `nums[i]` are added to the collection at step `i`.
      * **Removal of IDs:** If `freq[i]` is negative, it means `-freq[i]` IDs with the value `nums[i]` are removed from the collection at step `i`.
    
    Return an array `ans` of length `n`, where `ans[i]` represents the **count**
    of the most frequent ID in the collection after the `ith` step. If the
    collection is empty at any step, `ans[i]` should be 0 for that step.
    
    **Constraints:**
    
      * `1 <= nums.length == freq.length <= 10 ^ 5`
      * `1 <= nums[i] <= 10 ^ 5`
      * `-10 ^ 5 <= freq[i] <= 10 ^ 5`
      * `freq[i] != 0`
      * The input is generated such that the occurrences of an ID will not be negative in any step.
    """