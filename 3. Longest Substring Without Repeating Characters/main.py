'''
This program is to solve the LeetCode problem "3. Longest Substring Without Repeating Characters".
Author: Aman Kauroo
Date: 03/07/2026
'''
# s = "bbbbb"
# print(s)

# answer = []
# longest = 0

# string = list(s)
# print(string)

# for i in range(len(string)):
#     for j in range(i + 1, len(string)):
#         if string[j] not in answer:
#             answer.append(string[j])
#             if len(answer) > longest:
#                 longest = len(answer)


# print(answer)
# print(len(answer))
# print(longest)

'''
s = "abcabcbb"
longest = 0

for i in range(len(s)):
    seen = set()
    for j in range(i, len(s)):
        if s[j] in seen:
            break
        seen.add(s[j])
        longest = max(longest, len(seen))

print(longest)
'''

# Answer


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for i in range(len(s)):
            seen = set()

            for j in range(i, len(s)):
                if s[j] in seen:
                    break

                seen.add(s[j])
                longest = max(longest, len(seen))

        return longest
