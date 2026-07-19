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
    int maxDepth(TreeNode *root)
    {
        if (root == nullptr)
        {
            return 0;
        }
        queue<pair<TreeNode *, int>> queue;
        queue.push(make_pair(root, 1));
        int ans = 0;
        while (!queue.empty())
        {
            pair<TreeNode *, int> curr = queue.front();
            TreeNode *node = curr.first;
            int depth = curr.second;
            if (depth > ans)
            {
                ans = depth;
            }
            queue.pop();
            if (node->left != nullptr)
                queue.push(make_pair(node->left, depth + 1));
            if (node->right != nullptr)
                queue.push(make_pair(node->right, depth + 1));
        }
        return ans;
    }
};