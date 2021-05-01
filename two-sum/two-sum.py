class Solution:
    def twoSum(self, nums, target):
        for i, outer in enumerate(nums):
            for j, inner in enumerate(nums[i+1:]):
                if(outer + inner == target):
                    return [i,j+i+1]
