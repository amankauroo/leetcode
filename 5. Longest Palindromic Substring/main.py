'''
This program is to solve the LeetCode problem "5. Longest Palindromic Substring".
Author: Aman Kauroo
Date: 05/07/2026
'''
# Working Code:
# string = "babad"
# list = list(string)
# print(list)
# substring = []

# for i in range(len(list)):
#     for j in range(i, len(list)):
#         if list[i:j+1] == list[i:j+1][::-1]:
#             substring.append(list[i:j+1])

# length = 0
# for i in substring:
#     if len(i) > length:
#         length = len(i)
#         longest_palindrome = i


# print(longest_palindrome)

# Answer:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]

                if substring == substring[::-1]:
                    if len(substring) > len(longest_palindrome):
                        longest_palindrome = substring

        return longest_palindrome
