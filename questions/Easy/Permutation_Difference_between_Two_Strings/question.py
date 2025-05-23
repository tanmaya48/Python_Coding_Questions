def findPermutationDifference(s: str, t: str) -> int:
    """
    You are given two strings `s` and `t` such that every character occurs at most
    once in `s` and `t` is a permutation of `s`.
    
    The **permutation difference** between `s` and `t` is defined as the **sum**
    of the absolute difference between the index of the occurrence of each
    character in `s` and the index of the occurrence of the same character in `t`.
    
    Return the **permutation difference** between `s` and `t`.

    **Constraints:**
    
      * `1 <= s.length <= 26`
      * Each character occurs at most once in `s`.
      * `t` is a permutation of `s`.
      * `s` consists only of lowercase English letters.
    """
    diffs = [abs(s.index(c)-t.index(c)) for c in s]
    return sum(diffs)
