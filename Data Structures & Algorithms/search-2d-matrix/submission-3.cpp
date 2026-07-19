#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int top = 0;
        int bottom = rows - 1;
        while (top <= bottom)
        {
            int mid = (top + bottom) / 2;
            if (target > matrix[mid][cols - 1])
            {
                top = mid + 1;
            }
            else if (target < matrix[mid][0])
            {
                bottom = mid - 1;
            }
            else
            {
                break;
            }
        }
        if (!(top <= bottom))
        {
            return false;
        }
        int row = (top + bottom) / 2;
        int l = 0, r = cols - 1;
        while (l <= r)
        {
            int m = (l + r) / 2;
            if (target > matrix[row][m])
            {
                l = m + 1;
            }
            else if (target < matrix[row][m])
            {
                r = m - 1;
            }
            else
            {
                return true;
            }
        }
        return false;
    }
};
