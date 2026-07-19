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

class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        if (head == nullptr) {
            return;
        }
        if (head->next == nullptr) {
            return;
        }

        /* find the second half of the linked list */
        while (fast != nullptr && fast->next != nullptr) {
            fast = fast->next->next;
            slow = slow->next;
        }

        /* reverse second half of list */
        ListNode* temp;
        ListNode* prev = nullptr;
        while (slow != nullptr) {
            temp = slow->next;
            slow->next = prev;
            prev = slow;
            slow = temp;
        }

        ListNode *first = head;
        ListNode *second = prev;
        while (second != nullptr && second->next!= nullptr) {
            ListNode *temp1 = first->next;
            ListNode *temp2 = second->next;
            first->next = second;
            second->next = temp1;
            first = temp1;
            second = temp2;
        }
        
    }
};
