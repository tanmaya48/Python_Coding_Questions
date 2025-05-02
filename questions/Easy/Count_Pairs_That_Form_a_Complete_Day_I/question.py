from typing import List

def countCompleteDayPairs(hours: List[int]) -> int:
    """
    Given an integer array `hours` representing times in **hours** , return an
    integer denoting the number of pairs `i`, `j` where `i < j` and `hours[i] +
    hours[j]` forms a **complete day**.
    A **complete day** is defined as a time duration that is an **exact**
    **multiple** of 24 hours.  
    **Constraints:**
      * `1 <= hours.length <= 100`
      * `1 <= hours[i] <= 10 ^ 9`
    """
    count = 0
    l = len(hours)

    for i in range(l-1) : 
      for j in range(i+1, l) :
        if((hours[i] + hours[j]) % 24 == 0) :
          count+=1

    return count