# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 利用 slow & fast ptr 分成左半邊跟右半邊, 左半邊跟右半邊交叉合併
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        second_half_head = slow.next
        prev, slow.next = None, None # 斷開兩個 half
        
        while second_half_head:
            tmp = second_half_head.next # 把下個 node 暫存 tmp
            second_half_head.next = prev # ★ 將 curr 的 next 指到 prev
            prev = second_half_head # curr 設為 prev (prev 前進一格)
            second_half_head = tmp # 設 tmp 等於 curr (curr 前進一格)
        
        first_head, second_head = head, prev
        while second_head:
            tmp1, tmp2 = first_head.next, second_head.next
            first_head.next = second_head
            second_head.next = tmp1
            first_head, second_head = tmp1, tmp2
            
        