class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        sort(nums)
        for i in range(len(nums)):
            if -nums[i] in nums[i+1:]:
                return -nums[i]