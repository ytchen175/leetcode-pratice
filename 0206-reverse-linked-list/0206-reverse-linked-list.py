# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        
        if not head:
            return head

        while True:
            temp.append(head.val)
            if not head.next:
                break
            head = head.next

        # How to append new value in linked list?
        # 0_1. Initial a new linked list with temp[-1]
        results = ListNode(temp[-1])
        # 0_2. Assign a ptr for linked list
        curr = results

        # 1. New a node with value
        # 2. Assign prev_node.next = node
        # 3. Move ptr to this node
        for i in range(len(temp)-2, -1, -1): # NOTE: start iteration from temp[-2]
            now = ListNode(temp[i])
            curr.next = now
            curr = curr.next

        return results