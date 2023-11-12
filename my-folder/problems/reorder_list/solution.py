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
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        
        # reverse second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first_head, second_head = head, prev # prev 現在是最後一個 element
        
        # eg. [1, 2], [4, 3]
        while second_head:
            tmp1, tmp2 = first_head.next, second_head.next
            first_head.next = second_head # eg. [1, 4]
            second_head.next = tmp1 # eg. [1, 4, 2]
            first_head, second_head = tmp1, tmp2 # eg. first_head = 2, second_head = 3
