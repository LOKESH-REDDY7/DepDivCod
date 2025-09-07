# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        node = ListNode()
        less = []
        greater_equal = []
        cur = head
        start = ListNode()
        node = start
        while cur:
            if cur.val < x:
                less.append(cur)
            else:
                greater_equal.append(cur)
            cur = cur.next
        for less_item in less:
            if less_item != None:
                start.next = less_item
                less_item = less_item.next
                start = start.next
        for ge_item in greater_equal:
            if ge_item != None:
                start.next = ge_item
                ge_item = ge_item.next
                start = start.next
        start.next = None
        return node.next
        
        