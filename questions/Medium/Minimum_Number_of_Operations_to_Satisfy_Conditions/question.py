from typing import List

def minimumOperations(grid: List[List[int]]) -> int:
    """
    You are given a 2D matrix `grid` of size `m x n`. In one **operation** , you
    can change the value of **any** cell to **any** non-negative number. You need
    to perform some **operations** such that each cell `grid[i][j]` is:
    
      * Equal to the cell below it, i.e. `grid[i][j] == grid[i + 1][j]` (if it exists).
      * Different from the cell to its right, i.e. `grid[i][j] != grid[i][j + 1]` (if it exists).
    
    Return the **minimum** number of operations needed.
    
    **Constraints:**
    
      * `1 <= n, m <= 1000`
      * `0 <= grid[i][j] <= 9`
    """