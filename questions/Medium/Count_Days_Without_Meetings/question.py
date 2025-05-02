from typing import List




def countDays(days: int, meetings: List[List[int]]) -> int:
    """
    You are given a positive integer `days` representing the total number of days
    an employee is available for work (starting from day 1). You are also given a
    2D array `meetings` of size `n` where, `meetings[i] = [start_i, end_i]`
    represents the starting and ending days of meeting `i` (inclusive).
    Return the count of days when the employee is available for work but no
    meetings are scheduled.
    **Note:** The meetings may overlap.
    **Constraints:**
      * `1 <= days <= 10 ^ 9`
      * `1 <= meetings.length <= 10 ^ 5`
      * `meetings[i].length == 2`
      * `1 <= meetings[i][0] <= meetings[i][1] <= days`
    """
    available_days = [1 for i in range(days)]
    for m in meetings:
        start,end = m 
        for i in range(start,end+1):
            available_days[i-1] = 0
    return sum(available_days)


