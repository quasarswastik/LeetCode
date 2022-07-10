from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key= lambda a: a.start) #lambda, needs to get more comfortable or make a helper function
        for i in range(0, len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return 0
        return 1

