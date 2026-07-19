/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution
{
public:
    TreeNode *invertTree(TreeNode *root) {
        if (root == nullptr) {
            return nullptr;
        }
        stack<TreeNode*> stack;
        stack.push(root);
        while (!stack.empty()) {
            TreeNode* curr = stack.top();
            stack.pop();
            TreeNode* temp = curr->left;
            curr->left = curr->right;
            curr->right = temp;
            if (curr->left != nullptr)
                stack.push(curr->left);
            if (curr->right != nullptr)
            stack.push(curr->right);
        }
            return root;

    }
};