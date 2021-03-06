//
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(!head) return NULL;
        
        ListNode *prev = NULL;

        while(head!=NULL){
            ListNode *next = head->next;
            head->next = prev;
            prev = head;
            head = next;
        }
        
        return prev;
    }
};
