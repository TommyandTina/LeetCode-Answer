#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
# @lc code=end

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x=Counter(nums)
        for i,j in x.items():
            if j>1:
                return True
        return False

#O(n^2) in time and O(1) in space

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        nums.sort()
        for index, value in enumerate(nums):
            if value == nums[index-1]:
                return True
        return False
#O(nlogn) in time and O(1) in space