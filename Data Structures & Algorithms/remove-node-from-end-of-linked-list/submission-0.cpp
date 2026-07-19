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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int size = 0;
        ListNode* begin = head;
        while (begin != nullptr) {
          size += 1;
          begin = begin->next;
        }
        int remove = size - n;
        if (remove == 0) {
            return head->next;
        }
        ListNode* prev = head;
        ListNode* curr = head->next;
        for (int i = 1; i < remove; i++){
            prev = prev->next;
            curr = curr->next;
        }
        prev->next = curr->next;
        return head;
    }
};
