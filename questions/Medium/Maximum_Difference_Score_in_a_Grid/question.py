from typing import List

def maxScore(grid: List[List[int]]) -> int:
    """
    You are given an `m x n` matrix `grid` consisting of **positive** integers.
    You can move from a cell in the matrix to **any** other cell that is either to
    the bottom or to the right (not necessarily adjacent). The score of a move
    from a cell with the value `c1` to a cell with the value `c2` is `c2 - c1`.
    
    You can start at **any** cell, and you have to make **at least** one move.
    
    Return the **maximum** total score you can achieve.    
    
    **Constraints:**
    
      * `m == grid.length`
      * `n == grid[i].length`
      * `2 <= m, n <= 1000`
      * `4 <= m * n <= 10 ^ 5`
      * `1 <= grid[i][j] <= 10 ^ 5`
    """