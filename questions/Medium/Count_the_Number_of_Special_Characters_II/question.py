def numberOfSpecialChars(word: str) -> int:
    """
    You are given a string `word`. A letter `c` is called **special** if it
    appears **both** in lowercase and uppercase in `word`, and **every** lowercase
    occurrence of `c` appears before the **first** uppercase occurrence of `c`.
    Return the number of **special** letters in `word`.
    **Constraints:**
      * `1 <= word.length <= 2 * 10 ^ 5`
      * `word` consists of only lowercase and uppercase English letters.
    """
    rev_word = word[::-1]
    characters = 'abcdefghijklmnopqrstuvwxyz'
    word_len = len(word)
    specials =0
    for c in characters:
        if c not in word:
            continue
        if c.upper() not in word:
            continue
        if word_len - rev_word.index(c) -1 < word.index(c.upper()):
            specials+=1
    return specials

