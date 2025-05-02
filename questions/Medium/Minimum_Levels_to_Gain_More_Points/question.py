from typing import List

def minimumLevels(possible: List[int]) -> int:
    """
    You are given a binary array `possible` of length `n`.
    
    Alice and Bob are playing a game that consists of `n` levels. Some of the
    levels in the game are **impossible** to clear while others can **always** be
    cleared. In particular, if `possible[i] == 0`, then the `ith` level is
    **impossible** to clear for **both** the players. A player gains `1` point on
    clearing a level and loses `1` point if the player fails to clear it.
    
    At the start of the game, Alice will play some levels in the **given order**
    starting from the `0th` level, after which Bob will play for the rest of the
    levels.
    
    Alice wants to know the **minimum** number of levels she should play to gain
    more points than Bob, if both players play optimally to **maximize** their
    points.
    
    Return the**minimum** number of levels Alice should play to gain more
    points. If this is**not** possible, return `-1`.
    
    **Note** that each player must play at least `1` level.
    
    **Constraints:**
    
      * `2 <= n == possible.length <= 10 ^ 5`
      * `possible[i]` is either `0` or `1`.
    """