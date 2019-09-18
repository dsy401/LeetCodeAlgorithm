# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        list1 = ListNode(-1)
        list2 = list1
        pre = None
        while head:
            if head.val != pre:
                list2.next = ListNode(head.val)
                list2 = list2.next
                pre = head.val
            head = head.next
        return list1.next
