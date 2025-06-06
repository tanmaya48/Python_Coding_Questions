def numberOfChild(n: int, k: int) -> int:
    """
    You are given two **positive** integers `n` and `k`. There are `n` children
    numbered from `0` to `n - 1` standing in a queue _in order_ from left to
    right.
    
    Initially, child 0 holds a ball and the direction of passing the ball is
    towards the right direction. After each second, the child holding the ball
    passes it to the child next to them. Once the ball reaches **either** end of
    the line, i.e. child 0 or child `n - 1`, the direction of passing is
    **reversed**.
    
    Return the number of the child who receives the ball after `k` seconds.
    
    
    **Constraints:**
    
      * `2 <= n <= 50`
      * `1 <= k <= 50`
    """
    rounds,remaining = divmod(k,n-1)
    if rounds%2 == 0:
        return remaining
    return (n-1) - remaining
