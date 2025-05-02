def clearDigits(s: str) -> str:
    """
    You are given a string `s`.
    
    Your task is to remove **all** digits by doing this operation repeatedly:
    
      * Delete the first digit and the **closest** **non-digit** character to its left.
    
    Return the resulting string after removing all digits.
    
    **Constraints:**
    
      * `1 <= s.length <= 100`
      * `s` consists only of lowercase English letters and digits.
      * The input is generated such that it is possible to delete all digits.
    """
    l = len(s)
    newS = ''
    nums = '0123456789'
    for i in range(l) :
      if(s[i] in nums):
        newS = newS[:-1]
      else : 
        newS += s[i]
      # print(newS)
    return newS