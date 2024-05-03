class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        previous_value = 0

        for char in s:
            value = romanDict[char]
            #if the previous_value < current value, we minus that val 2 times
            if previous_value < value:
                result += value - 2*previous_value
            else:
                result += value
            previous_value = value
        return result