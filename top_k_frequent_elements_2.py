class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        expect = {}
        for i in nums:
            if i not in expect:
                expect[i] = 1
            else:
                expect[i] += 1
        
        expect_sorted = sorted(expect.items(), key = lambda x:x[1], reverse=True)
        
        outs = []
        for i in range(k):
            outs.append(expect_sorted[i][0])

        return outs
