'''
This program is to solve the LeetCode problem "2. Adding Two Numbers".
Author: Aman Kauroo
Date: 02/07/2026
'''

'''
def addTwoNumbers(l1, l2):
    l1.append(0)

    longest = None
    shortest = None

    if len(l1) > len(l2):
        longest = l1
        shortest = l2
    else:
        longest = l2
        shortest = l1

    for i in range(len(longest) - len(shortest)):
        shortest.append(0)

    buffer = 0
    l3 = []

    print(len(l1))
    print(len(l2))

    for i in range(len(l1)):
        sum = l1[i] + l2[i] + buffer
        if sum >= 10:
            sum = sum - 10
            buffer = 1
        else:
            buffer = 0
        l3.append(sum)

    if l3[-1] == 0:
        l3.pop()
    print(l3)

# l1 = [2, 4, 3]
# l2 = [5, 6, 4]

# l1 = [0]
# l2 = [0]

l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]

print(addTwoNumbers(l1, l2))

'''

# Answer:


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
