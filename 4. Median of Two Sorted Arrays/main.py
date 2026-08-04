'''
This program is to solve the LeetCode problem "4. Median of Two Sorted Arrays".
Author: Aman Kauroo
Date: 04/07/2026
'''
# Input: nums1 = [1, 3], nums2 = [2]
# Output: 2.00000
# Input: nums1 = [1, 2], nums2 = [3, 4]
# Output: 2.50000

# check if number is even or odd
# number = 5
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

'''
num1 = [1, 3, 24, 67, 89, 33, 45, 56, 78, 90, 94, 34, 22, 17]
num2 = [2, 4]

merged_array = sorted(num1 + num2)
print(merged_array)
print(len(merged_array))
length = len(merged_array)

if length % 2 == 0:
    print("Even")
    median = (merged_array[length // 2 - 1] + merged_array[length // 2]) / 2
    print("Median: ", median)

else:
    print("Odd")
    median = length // 2
    print("Median: ", merged_array[median])
'''

# Anwser:


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)

        if n % 2 == 0:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
        else:
            return float(merged[n // 2])
