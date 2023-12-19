/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

//Another approach is tried witht the python code. But better is this approach
//just traversing the LLs and add them acoordingly
//by converting into number first may lead to error because if number is really big with 100 digit
//any datatype can't hold it. So, will lead to outside range error.

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* listnum=NULL,*itr;
        int carry=0;
        while(l1 || l2 || carry){
            int n1=0,n2=0;
            if(l1!=NULL)
                n1=l1->val;
            if(l2!=NULL)
                n2=l2->val;
            int num = n1 + n2 + carry;
            int digit = num%10;
            carry = num/10;
            ListNode *temp = new ListNode();
            temp->val=digit;
            if(listnum==NULL){
                listnum=temp;
                itr=listnum;
            }
            else{
                itr->next=temp;
                itr=temp;
            }
            if(l1!=NULL){
                l1=l1->next;
            }
            if(l2!=NULL){
                l2=l2->next;
            }
        }
        return listnum;
    }
};
