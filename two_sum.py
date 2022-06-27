# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_indices = {}
        for i in range(len(nums)):
            if target - nums[i] in number_indices:
                return number_indices[target - nums[i]], i
            number_indices[nums[i]] = i
