def isSubstringPresent(s: str) -> bool:
    """
    Given a string `s`, find any substring of length `2` which is also present
    in the reverse of `s`.
    
    Return `true` if such a substring exists, and `false` otherwise.

    **Constraints:**
    
      * `1 <= s.length <= 100`
      * `s` consists only of lowercase English letters.
    """
    for i in range(len(s)):
        substring = s[i:i+2][::-1]
        if len(substring) == 1:
            return False
        if substring in s:
            return True
    return False


isSubstringPresent('abca')
