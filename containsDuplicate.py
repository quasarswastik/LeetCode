class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = {}
        for i in nums:
            if i not in numbers:
                numbers[i] = 1
            else:
                return 1
        return 0
