class Solution:
    def climbStairs(self, n: int) -> int:
        output = 0
        fibo_list = []
        fibo_list.append(1)
        fibo_list.append(2)
        for i in range(2,n):
            fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
            output = fibo_list[-1]
        return output if n > 2 else n

#Another solution for fibonacci series
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range (n -1):
            temp = one
            one = one + two
            two = temp

        return one