class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = defaultdict(list)
        
        for i in strs:
            characters = [0] * 26 # 26 0s
            for j in i:
                characters[ord(j) - ord('a')] += 1
            sets[tuple(characters)].append(i)
        
        return sets.values()
        
