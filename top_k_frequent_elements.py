class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = {}
        freq_to_num = [[]] * (len(nums) + 1)
        temp = 0
        print(freq_to_num)
        for i in range(len(freq_to_num)):
            freq_to_num[i].append(temp) #.append(temp)
            temp += 1
            # print(temp)
        
        for i in nums:
            if i not in nums_freq:
                nums_freq[i] = 1
            else:
                nums_freq[i] = 1 + nums_freq[i]
        print(nums_freq)
        print(freq_to_num)
        for n, c in nums_freq.items():
            freq_to_num[c].append(n)
            
        result = []
        for i in range(len(freq_to_num) - 1, 0, -1):
            for n in freq_to_num[i]:
                result.append(n)
                if len(result) == k:
                    return result
                
