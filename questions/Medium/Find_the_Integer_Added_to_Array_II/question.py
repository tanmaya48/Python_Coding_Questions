from typing import List


def check_match(nums1,nums2):
    diffs = 0
    for val in set(nums1):
        diffs += abs(nums1.count(val) - nums2.count(val))
    return diffs <= 2


def minimumAddedInteger(nums1: List[int], nums2: List[int]) -> int:
    """
    You are given two integer arrays `nums1` and `nums2`.
    From `nums1` two elements have been removed, and all other elements have been
    increased (or decreased in the case of negative) by an integer, represented by
    the variable `x`.
    As a result, `nums1` becomes **equal** to `nums2`. Two arrays are considered
    **equal** when they contain the same integers with the same frequencies.
    Return the **minimum** possible integer `x` that achieves this
    equivalence.
    **Constraints:**
      * `3 <= nums1.length <= 200`
      * `nums2.length == nums1.length - 2`
      * `0 <= nums1[i], nums2[i] <= 1000`
      * The test cases are generated in a way that there is an integer `x` such that `nums1` can become equal to `nums2` by removing two elements and adding `x` to each element of `nums1`.
    """
    for i in range(-1000,1001):
        add_case = [val+i for val in nums2]
        #if check_match(nums1,add_case):
            #return -i
        sub_case = [val-i for val in nums2]
        if check_match(nums1,sub_case):
            return i


