class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right - left > 0:
            print (left)
            print (right)
            print (nums[left+right//2] )
            if (nums[left+right//2] < target):
                left = left+right//2 + 1
            elif (nums[left+right//2] > target):
                right = left+right//2 - 1
            else:
                return left+right//2
        return -1
