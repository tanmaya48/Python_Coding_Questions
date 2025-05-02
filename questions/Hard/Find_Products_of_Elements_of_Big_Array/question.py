from typing import List

def findProductsOfElements(queries: List[List[int]]) -> List[int]:
    """
    A **powerful array** for an integer `x` is the shortest sorted array of powers
    of two that sum up to `x`. For example, the powerful array for 11 is `[1, 2,
    8]`.
    
    The array `big_nums` is created by concatenating the **powerful** arrays for
    every positive integer `i` in ascending order: 1, 2, 3, and so forth. Thus,
    `big_nums` starts as `[_1_ , _2_ , _1, 2_ , _4_ , _1, 4_ , _2, 4_ , _1, 2, 4_
    , _8_ , ...]`.
    
    You are given a 2D integer matrix `queries`, where for `queries[i] = [fromi,
    toi, modi]` you should calculate `(big_nums[fromi] * big_nums[fromi + 1] * ...
    * big_nums[toi]) % modi`.
    
    Return an integer array `answer` such that `answer[i]` is the answer to the
    `ith` query.
    
    **Constraints:**
    
      * `1 <= queries.length <= 500`
      * `queries[i].length == 3`
      * `0 <= queries[i][0] <= queries[i][1] <= 10 ^ 15`
      * `1 <= queries[i][2] <= 10 ^ 5`
    """