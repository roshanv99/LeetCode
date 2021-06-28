#My Sol

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is not None:
            odd = head
            odd_start = head
        else:
            return head
        
        if head.next is not None:
            even = head.next
            even_start = head.next
        else:
            return head
        
        while(odd or even is not None):
                   
            if odd.next is not None:
                if even.next is not None:
                    odd.next = even.next
                    odd = odd.next
                else: 
                    odd.next = None
                    break
            if even.next is not None:
                if odd.next is not None:
                    even.next = odd.next
                    even = even.next
                else:
                    even.next = None
                    break
            

                
        odd.next = even_start        
        return odd_start
        
            
            
        
