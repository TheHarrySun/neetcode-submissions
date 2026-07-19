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
    int goodNodes(TreeNode *root)
    {
        if (root == nullptr)
        {
            return 0;
        }

        queue<pair<TreeNode *, int>> tree;

        tree.push(make_pair(root, root->val));
        int res = 0;

        while (!tree.empty())
        {
            pair<TreeNode *, int> curr = tree.front();
            tree.pop();
            if (curr.first->left != nullptr)
                tree.push(make_pair(curr.first->left, max(curr.first->val, curr.second)));
            if (curr.first->right != nullptr)
                tree.push(make_pair(curr.first->right, max(curr.first->val, curr.second)));
            if (curr.first->val >= curr.second)
            {
                res += 1;
            }
        }
        return res;
    }
};