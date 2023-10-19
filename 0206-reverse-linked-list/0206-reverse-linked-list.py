# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while (curr):
            nxt = curr.next # 先把 curr 的下一個 node 暫存起來變成 nxt
            curr.next = prev # 調換 ptr 方向，顛倒過來
            prev = curr # 把 curr 設成 prev 
            curr = nxt # 跳到下一個 node

        return prev