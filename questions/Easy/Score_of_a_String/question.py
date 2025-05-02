def scoreOfString(s: str) -> int:
    """
    You are given a string `s`. The **score** of a string is defined as the sum of
    the absolute difference between the **ASCII** values of adjacent characters.
    Return the **score** of `s`.    
    **Constraints:**
      * `2 <= s.length <= 100`
      * `s` consists only of lowercase English letters.
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    score = 0
    for i in range(len(s)-1):
        score += abs(letters.index(s[i]) - letters.index(s[i+1]))
    return score

