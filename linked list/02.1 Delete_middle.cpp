//Delete the middle element of Linked list
class Solution{
    public:
    Node* deleteMid(Node* head)
    {
        if(head==NULL || head->next==NULL){
            return NULL;
        }
        Node *slow = head, *fast = head, *slowest=NULL;
        while(fast->next!=NULL){
            slowest=slow;
            slow=slow->next;
            if(fast->next->next==NULL){
                break;
            }
            fast=fast->next->next;
        }
        slowest->next=slow->next;
        delete slow;
        return head;
    }
};
