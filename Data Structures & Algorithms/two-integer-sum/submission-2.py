class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
            x = target - v
            if x in nums:
                if(i==nums.index(x)):
                    continue
                return sorted([nums.index(x),i])
