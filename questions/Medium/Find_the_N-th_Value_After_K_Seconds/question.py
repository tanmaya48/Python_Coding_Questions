def valueAfterKSeconds(n: int, k: int) -> int:
    """
    You are given two integers `n` and `k`.
    
    Initially, you start with an array `a` of `n` integers where `a[i] = 1` for
    all `0 <= i <= n - 1`. After each second, you simultaneously update each
    element to be the sum of all its preceding elements plus the element itself.
    For example, after one second, `a[0]` remains the same, `a[1]` becomes `a[0] +
    a[1]`, `a[2]` becomes `a[0] + a[1] + a[2]`, and so on.
    
    Return the **value** of `a[n - 1]` after `k` seconds.
    
    Since the answer may be very large, return it **modulo** `10 ^ 9 + 7`.
    
    **Constraints:**
    
      * `1 <= n, k <= 1000`
    """