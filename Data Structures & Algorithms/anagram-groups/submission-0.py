class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = {}

        for s in strs:
            sortted = ''.join(sorted(s))
            if sortted not in group:
                group[sortted] = []
            group[sortted].append(s)
        
        return list(group.values())

