from typing import List

def maxTotalReward(rewardValues: List[int]) -> int:
    """
    You are given an integer array `rewardValues` of length `n`, representing the
    values of rewards.
    
    Initially, your total reward `x` is 0, and all indices are **unmarked**. You
    are allowed to perform the following operation **any** number of times:
    
      * Choose an **unmarked** index `i` from the range `[0, n - 1]`.
      * If `rewardValues[i]` is **greater** than your current total reward `x`, then add `rewardValues[i]` to `x` (i.e., `x = x + rewardValues[i]`), and **mark** the index `i`.
    
    Return an integer denoting the **maximum** total reward you can collect by
    performing the operations optimally.
    
    **Constraints:**
    
      * `1 <= rewardValues.length <= 5 * 10 ^ 4`
      * `1 <= rewardValues[i] <= 5 * 10 ^ 4`
    """