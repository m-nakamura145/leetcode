class Solution:
    def runningSum(self, nums):
        result = []
        tmp = 0
        for i, value in enumerate(nums):
            result.append(tmp + value)
            tmp = result[i]
        return result
