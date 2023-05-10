class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sequence = set(nums)
        longestSeq = 0
        length = 0

        for i in sequence:
            if i-1 not in sequence:
                length = 0
                while (i+length) in sequence:
                    length += 1
                longestSeq = max(length, longestSeq)
        
        return longestSeq
