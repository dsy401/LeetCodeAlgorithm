# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        temp = head
        list_temps = []
        while temp != None:
            list_temps.append(temp)
            if temp.next in list_temps:
                return True
            else:
                temp = temp.next
        return False