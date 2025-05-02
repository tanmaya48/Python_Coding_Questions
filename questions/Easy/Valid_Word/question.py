
vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
numbers = '0123456789'
valid_letters = vowels+consonants+numbers


def isValid(word: str) -> bool:
    """
    A word is considered **valid** if:
      * It contains a **minimum** of 3 characters.
      * It contains only digits (0-9), and English letters (uppercase and lowercase).
      * It includes **at least** one **vowel**.
      * It includes **at least** one **consonant**.
    You are given a string `word`.
    Return `true` if `word` is valid, otherwise, return `false`.
    **Notes:**
      * `'a'`, `'e'`, `'i'`, `'o'`, `'u'`, and their uppercases are **vowels**.
      * A **consonant** is an English letter that is not a vowel.
    **Constraints:**
      * `1 <= word.length <= 20`
      * `word` consists of English uppercase and lowercase letters, digits, `'@'`, `'#'`, and `'$'`.
    """
    if len(word) <3:
        return False
    if sum([1 for c in vowels if c in word]) <1:
        return False
    if sum([1 for c in consonants if c in word]) <1:
        return False
    for c in word:
        if c not in valid_letters:
            return False
    return True
    

#isValid('234ag')
