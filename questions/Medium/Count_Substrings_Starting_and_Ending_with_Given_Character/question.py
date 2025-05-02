
def countSubstrings(s: str, c: str) -> int:
    """
    You are given a string `s` and a character `c`. Return the total number of
    substrings of `s` that start and end with `c`.
    **Constraints:**
      * `1 <= s.length <= 10 ^ 5`
      * `s` and `c` consist only of lowercase English letters.
    """
    positions = s.count(c)
    if positions == 0:
        return 0
    return sum(i for i in range(positions+1))
    




