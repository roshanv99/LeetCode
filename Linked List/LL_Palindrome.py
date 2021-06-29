#Application of Floyd's Algorithm again
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        
        #Get slow till the middle and fast till the end
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            
        prev, slow, prev.next = slow, slow.next, None
        
        #Reverse Direction so that end to middle points to the middle
        while slow:
            temp = slow.next
            slow.next, prev, slow = prev, slow, temp
        fast, slow = head, prev
        
        #Comparison
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True
