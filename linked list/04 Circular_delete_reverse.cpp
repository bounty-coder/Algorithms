// Given a Circular Linked List.
// The task is to delete the given node, key in the circular linked list(delete first key) 
// and reverse the circular linked list.

class Solution {
  public:
    // Function to reverse a circular linked list
    Node* reverse(Node* head) {
        if (head == nullptr || head->next == head) return head;
        Node* prev = nullptr;
        Node* curr = head;
        Node* frw = head->next;

        while (frw != head) {
            curr->next = prev;
            prev = curr;
            curr = frw;
            frw = frw->next;
        }
        curr->next = prev;
        frw->next = curr; 

        return curr;
    }

    // Function to delete a node from the circular linked list
    Node* deleteNode(Node* head, int key) {
         if (head == nullptr) return head; 

        Node* temp = head;
        if (head->data == key) {
            if (head->next == head) {
                delete head;
                return nullptr;
            }
            while (temp->next != head) {
                temp = temp->next;
            }
            temp->next = head->next;
            Node* toDelete = head;
            head = head->next; 
            delete toDelete;
            return head;
        }

        while (temp->next != head && temp->next->data != key) {
            temp = temp->next;
        }
        if (temp->next->data == key) {
            Node* toDelete = temp->next;
            temp->next = temp->next->next;
            delete toDelete;
        }

        return head;
    }
};
