class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = {}

        for num in nums:
            if num not in result:
                result[num] = 0
            result[num] += 1
        
        sorted_items = sorted(result.items(), key=lambda item: item[1], reverse = True)

        return [item[0] for item in sorted_items[:k]]