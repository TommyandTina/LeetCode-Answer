class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        after_remove_pos = 0
        duplicates = 0
        for i in range (0, len(nums)):
            if nums[i] != val:
                nums[after_remove_pos] = nums[i]
                after_remove_pos += 1
        return after_remove_pos
        