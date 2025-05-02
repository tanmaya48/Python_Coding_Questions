from typing import List

def findWinningPlayer(skills: List[int], k: int) -> int:
    """
    A competition consists of `n` players numbered from `0` to `n - 1`.
    You are given an integer array `skills` of size `n` and a **positive** integer
    `k`, where `skills[i]` is the skill level of player `i`. All integers in
    `skills` are **unique**.
    All players are standing in a queue in order from player `0` to player `n -
    1`.
    The competition process is as follows:
      * The first two players in the queue play a game, and the player with the **higher** skill level wins.
      * After the game, the winner stays at the beginning of the queue, and the loser goes to the end of it.
    The winner of the competition is the **first** player who wins `k` games **in
    a row**.
    Return the initial index of the winning player.
    **Constraints:**
      * `n == skills.length`
      * `2 <= n <= 10 ^ 5`
      * `1 <= k <= 10 ^ 9`
      * `1 <= skills[i] <= 10 ^ 6`
      * All integers in `skills` are unique.
    """
    for i,val in enumerate(skills):
        competition = skills[i+1:]
        wins = 0
        if i > 0:
            if val > skills[i-1]:
                wins+=1
        for c in competition:
            if wins >= k:
                return i 
            if c > val:
                break
            wins+=1
    # no one has won till the first round, meaning the max will win
    return skills.index(max(skills))

