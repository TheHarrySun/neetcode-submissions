/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node *, Node *> map;
        
        Node *begin = head;
        while (begin != nullptr) {
            Node *new_node = new Node(begin->val);
            map.insert({begin, new_node});
            begin = begin->next;
        }

        begin = head;
        while (begin != nullptr) {
            Node *curr = map[begin];
            if (begin->next == nullptr) {
                curr->next = nullptr;
            }
            else {
            curr->next = map[begin->next];
            }
            if (begin->random == nullptr) {
                curr->random == nullptr;
            }
            else {
                curr->random = map[begin->random];
            }
            begin = begin->next;
        }
        return map[head];
    }
};
