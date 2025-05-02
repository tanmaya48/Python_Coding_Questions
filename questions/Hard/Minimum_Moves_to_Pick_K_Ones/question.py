from typing import List

def minimumMoves(nums: List[int], k: int, maxChanges: int) -> int:
    """
    You are given a binary array `nums` of length `n`, a **positive** integer `k`
    and a **non-negative** integer `maxChanges`.
    
    Alice plays a game, where the goal is for Alice to pick up `k` ones from
    `nums` using the **minimum** number of **moves**. When the game starts, Alice
    picks up any index `aliceIndex` in the range `[0, n - 1]` and stands there. If
    `nums[aliceIndex] == 1` , Alice picks up the one and `nums[aliceIndex]`
    becomes `0`(this **does not** count as a move). After this, Alice can make
    **any** number of **moves** (**including** **zero**) where in each move Alice
    must perform **exactly** one of the following actions:
    
      * Select any index `j != aliceIndex` such that `nums[j] == 0` and set `nums[j] = 1`. This action can be performed **at** **most** `maxChanges` times.
      * Select any two adjacent indices `x` and `y` (`|x - y| == 1`) such that `nums[x] == 1`, `nums[y] == 0`, then swap their values (set `nums[y] = 1` and `nums[x] = 0`). If `y == aliceIndex`, Alice picks up the one after this move and `nums[y]` becomes `0`.
    
    Return the**minimum** number of moves required by Alice to pick
    **exactly** `k` ones.
    
    **Constraints:**
    
      * `2 <= n <= 10 ^ 5`
      * `0 <= nums[i] <= 1`
      * `1 <= k <= 10 ^ 5`
      * `0 <= maxChanges <= 10 ^ 5`
      * `maxChanges + sum(nums) >= k`
    """