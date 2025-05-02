from typing import List

def minimumSubstringsInPartition(s: str) -> int:
    """
    Given a string `s`, you need to partition it into one or more **balanced**
    substrings. For example, if `s == "ababcc"` then `("abab", "c", "c")`, `("ab",
    "abc", "c")`, and `("ababcc")` are all valid partitions, but `("a", **"
    bab"**, "cc")`, `(**" aba"**, "bc", "c")`, and `("ab", **" abcc"**)` are not.
    The unbalanced substrings are bolded.
    
    Return the **minimum** number of substrings that you can partition `s` into.
    
    **Note:** A **balanced** string is a string where each character in the string
    occurs the same number of times.    
    
    **Constraints:**
    
      * `1 <= s.length <= 1000`
      * `s` consists only of English lowercase letters.
    """