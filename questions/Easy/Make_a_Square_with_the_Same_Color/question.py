from typing import List


def get_same_count(mat,i,j):
    w = 0
    w+= 1 if mat[i][j] == 'W' else 0
    w+= 1 if mat[i+1][j] == 'W' else 0
    w+= 1 if mat[i+1][j+1] == 'W' else 0
    w+= 1 if mat[i][j+1] == 'W' else 0
    return max(w,4-w)

def canMakeSquare(grid: List[List[str]]) -> bool:
    """
    You are given a 2D matrix `grid` of size `3 x 3` consisting only of characters
    `'B'` and `'W'`. Character `'W'` represents the white color, and character
    `'B'` represents the black color.
    Your task is to change the color of **at most one** cell so that the matrix
    has a `2 x 2` square where all cells are of the same color.
    Return `true` if it is possible to create a `2 x 2` square of the same color,
    otherwise, return `false`.
    **Constraints:**
    
      * `grid.length == 3`
      * `grid[i].length == 3`
      * `grid[i][j]` is either `'W'` or `'B'`.
    """
    for i in range(2):
        for j in range(2):
            if get_same_count(grid,i,j) >= 3:
                return True
    return False

    
