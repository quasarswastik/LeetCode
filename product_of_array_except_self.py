class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        
        prefix = 1
        for i in range(0, len(nums) - 1, 1):
            prefix = prefix*nums[i]
            result.append(prefix)
            print(prefix)
        postfix = 1 
        for i in range(len(nums)-1, -1, -1):
            result[i] = postfix * result[i]
            print(postfix)
            postfix = postfix*nums[i]
        
        return result
