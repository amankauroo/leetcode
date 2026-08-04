'''
This program is to solve the LeetCode problem "1. Two Sums".
Author: Aman Kauroo
Date: 01/07/2026
'''


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)
print(result)
