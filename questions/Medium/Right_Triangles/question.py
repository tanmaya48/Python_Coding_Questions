from typing import List

def numberOfRightTriangles(grid: List[List[int]]) -> int:
    """
    You are given a 2D boolean matrix `grid`.
    
    Return an integer that is the number of **right triangles** that can be made
    with the 3 elements of `grid` such that **all** of them have a value of 1.
    
    **Note:**
    
      * A collection of 3 elements of `grid` is a **right triangle** if one of its elements is in the **same row** with another element and in the **same column** with the third element. The 3 elements do not have to be next to each other.

    **Constraints:**
    
      * `1 <= grid.length <= 1000`
      * `1 <= grid[i].length <= 1000`
      * `0 <= grid[i][j] <= 1`
    """
    h = len(grid)
    w = len(grid[0])
    triangles = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 0:
                continue
            b = sum(grid[y]) -1
            t = sum([grid[i][x] for i in range(h)]) -1
            triangles+= (t*b)
    return triangles

numberOfRightTriangles([[0,1],[1,1]])
