def minOperations(k: int) -> int:
    """
    You are given a **positive** integer `k`. Initially, you have an array `nums =
    [1]`.
    You can perform **any** of the following operations on the array **any**
    number of times (**possibly zero**):
      * Choose any element in the array and **increase** its value by `1`.
      * Duplicate any element in the array and add it to the end of the array.
    Return the **minimum** number of operations required to make the **sum** of
    elements of the final array greater than or equal to `k`.
    **Constraints:**
      * `1 <= k <= 10 ^ 5`
    """
    num = 1
    if num >= k:
        return 0
    while True:
        if num * (num) >= k:
            return (2*num) -2
        if num * (num+1) >= k:
            return (2*num) -1
        num+=1


