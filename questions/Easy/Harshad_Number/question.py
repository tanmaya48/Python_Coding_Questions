def sumOfTheDigitsOfHarshadNumber(x: int) -> int:
    """
    An integer divisible by the **sum** of its digits is said to be a **Harshad**
    number. You are given an integer `x`. Return the sum of the digits of `x` 
    if `x` is a **Harshad** number, otherwise, return `-1`.
    
    **Constraints:**
    
      * `1 <= x <= 100`
    """
    sum_of_digits = 0
    val = x
    while val > 0:
        sum_of_digits += val%10
        val = val//10
    if x%sum_of_digits == 0:
        return sum_of_digits
    return -1
    
