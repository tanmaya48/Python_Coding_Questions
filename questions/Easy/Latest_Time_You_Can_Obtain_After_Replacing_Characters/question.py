def findLatestTime(s: str) -> str:
    """
    You are given a string `s` representing a 12-hour format time where some of
    the digits (possibly none) are replaced with a `"?"`.
    12-hour times are formatted as `"HH:MM"`, where `HH` is between `00` and `11`,
    and `MM` is between `00` and `59`. The earliest 12-hour time is `00:00`, and
    the latest is `11:59`.
    You have to replace **all** the `"?"` characters in `s` with digits such that
    the time we obtain by the resulting string is a **valid** 12-hour format time
    and is the **latest** possible.
    Return the resulting string.
    **Constraints:**
      * `s.length == 5`
      * `s[2]` is equal to the character `":"`.
      * All characters except `s[2]` are digits or `"?"` characters.
      * The input is generated such that there is **at least** one time between `"00:00"` and `"11:59"` that you can obtain after replacing the `"?"` characters.
    """
    digits = [c for c in s if c != ':']
    if digits[0] == '0' and digits[1] == '?':
        digits[1] = '9'
    #
    elif digits[0] == '?':
        if digits[1] in '01?':
            digits[0] = '1'
        else:
            digits[0] = '0'
    #
    if digits[0] == '1' and digits[1] == '?':
        digits[1] = '1'
    #
    if digits[2] == '?':
        digits[2] = '5'
    #
    if digits[3] == '?':
        digits[3] = '9'
    a,b,c,d = digits
    return f"{a}{b}:{c}{d}"

