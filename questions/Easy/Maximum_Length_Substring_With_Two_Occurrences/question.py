def maximumLengthSubstring(s: str) -> int:
    """
    Given a string `s`, return the **maximum** length of a substring such that it
    contains at most two occurrences of each character.
    **Constraints:**
      * `2 <= s.length <= 100`
      * `s` consists only of lowercase English letters.
    """
    start = 0
    longest = 0
    while True:
        if start == len(s) -1:
            break
        tripled = False
        for end in range(start+1,len(s)):
            substring = s[start:end+1]
            if len(substring) <3:
                continue
            chars = set(substring)
            for c in chars:
                if substring.count(c) > 2:
                    tripled = True
                    break
            if tripled:
                break
        if tripled:
            length = len(substring)-1
        else:
            length = len(substring)
        longest = max(longest,length)
        start+=1
    return longest



print(maximumLengthSubstring('aaaa'))
