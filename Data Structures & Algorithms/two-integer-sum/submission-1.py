class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i in range(len(nums)):
            search_num = target - nums[i]  
            if search_num not in result:
                result[nums[i]] = i
            else:
                return [result[search_num], i]
        