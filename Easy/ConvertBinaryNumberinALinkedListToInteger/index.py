# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getDecimalValue(self, head):

        bin_digit = ""

        while head != None:
            current = head.val
            bin_digit += str(current)
            head = head.next

        return self.bin_to_hex(bin_digit)

    def bin_to_hex(self,s):
        hex = 0
        for i in range(len(s)):
            if s[i] == '0':
                hex += 0
            else:
                hex += 2 ** (len(s)-1-i)

        return hex



list1 = ListNode(1)
list1.next = ListNode(0)
list1.next.next = ListNode(1)
a = Solution()
print(a.getDecimalValue(list1))