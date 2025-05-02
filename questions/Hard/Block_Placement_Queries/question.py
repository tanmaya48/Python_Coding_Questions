from typing import List



def can_place(block,obstacles):
    max_x, size = block
    last_place = max_x - size
    if last_place <0:
        return False
    for start in range(last_place+1):
        end = start+ size
        overlapped = False
        for obs in obstacles:
            if obs>start and obs < end:
                overlapped=True
                break
        if not overlapped:
            return True
    return False
        



def getResults(queries: List[List[int]]) -> List[bool]:
    """
    There exists an infinite number line, with its origin at 0 and extending
    towards the **positive** x-axis.
    
    You are given a 2D array `queries`, which contains two types of queries:
    
      1. For a query of type 1, `queries[i] = [1, x]`.
         Build an obstacle at distance `x` from the origin. 
         It is guaranteed that there is **no** obstacle at distance `x` when the query is asked.

      2. For a query of type 2, `queries[i] = [2, x, sz]`. 
         Check if it is possible to place a block of size `sz` anywhere in the range `[0, x]` 
         on the line, such that the block **entirely** lies in the range `[0, x]`. 
         A block **cannot** be placed if it intersects with any obstacle, but it may touch it. 
         Note that you do**not** actually place the block. Queries are separate.
    
    Return a boolean array `results`, where `results[i]` is `true` if you can
    place the block specified in the `ith` query of type 2, and `false` otherwise.
    
    **Constraints:**
    
      * `1 <= queries.length <= 15 * 10 ^ 4`
      * `2 <= queries[i].length <= 3`
      * `1 <= queries[i][0] <= 2`
      * `1 <= x, sz <= min(5 * 10 ^ 4, 3 * queries.length)`
      * The input is generated such that for queries of type 1, no obstacle exists at distance `x` when the query is asked.
      * The input is generated such that there is at least one query of type 2.
    """
    obstacles = []
    results = []
    for q in queries:
        if q[0] == 1:
            obstacles.append(q[1])
        else:
            results.append(can_place(q[1:],obstacles) )
    return results

#print(getResults([[1,2],[2, 2, 2]]))
