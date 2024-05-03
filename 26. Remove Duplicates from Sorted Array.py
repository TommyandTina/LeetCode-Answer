class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Starting at 2nd index
        unique_pos = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[unique_pos] = nums[i]
                unique_pos += 1
        return unique_pos

#Better time execution solution
sys.stdout=open('user.out','w')

for nums in map(loads,stdin):
    nums=sorted(list(set(nums)))
    print('[',end='')
    print(*(i for i in nums),sep=',',end='')
    print(']')
exit()
"""
Set có thể xóa được các trùng lặp
sort chỉ sort được list nên set phải được chuyển về list
Dấu * là unpack generator, dùng được cho tuple, set, generator expression
map(loads,stdin) là để chuyển nhiều list trong stdin vào thành từng list để xử lý
"""