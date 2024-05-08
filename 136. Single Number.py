class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i

#another solution
    def singleNumber(self, nums: List[int]) -> int:
        x=Counter(nums)
        for i , j in x.items():
            if j>1:
                continue
            else:
                return i

"""
Ghi chú về Counter:

# A Python program to show different ways to create
# Counter
from collections import Counter
 
# With sequence of items 
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
 
# with dictionary
print(Counter({'A':3, 'B':5, 'C':2}))
 
# with keyword arguments
print(Counter(A=3, B=5, C=2))

"""