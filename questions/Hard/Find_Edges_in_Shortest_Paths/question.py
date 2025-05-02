from typing import List

def findAnswer(n: int, edges: List[List[int]]) -> List[bool]:
    """
    You are given an undirected weighted graph of `n` nodes numbered from 0 to `n
    - 1`. The graph consists of `m` edges represented by a 2D array `edges`, where
    `edges[i] = [ai, bi, wi]` indicates that there is an edge between nodes `ai`
    and `bi` with weight `wi`.
    
    Consider all the shortest paths from node 0 to node `n - 1` in the graph. You
    need to find a **boolean** array `answer` where `answer[i]` is `true` if the
    edge `edges[i]` is part of **at least** one shortest path. Otherwise,
    `answer[i]` is `false`.
    
    Return the array `answer`.
    
    **Note** that the graph may not be connected.
    
    **Constraints:**
    
      * `2 <= n <= 5 * 10 ^ 4`
      * `m == edges.length`
      * `1 <= m <= min(5 * 10 ^ 4, n * (n - 1) / 2)`
      * `0 <= ai, bi < n`
      * `ai != bi`
      * `1 <= wi <= 10 ^ 5`
      * There are no repeated edges.
    """