class Solution:
    def search(self, nums: List[int], target: int) -> int:
        half = int(len(nums) / 2)
        length = len(nums) - 1
        if (nums[half] == target):
            return half-1
        elif (nums[half] > target):
            search(nums[0 : half], target)
        elif (nums[half] < target):
            search(nums[half:length], target) 
        return -1
