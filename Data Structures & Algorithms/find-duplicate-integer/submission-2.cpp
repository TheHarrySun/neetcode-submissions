/* ----------------------------------------------------- */
/* FindDuplicate.cpp                                     */
/* Author: Harrison Xu                                   */
/* Email: hx2004@princeton.edu                           */
/* ----------------------------------------------------- */

/* LeetCode Problem: Find the Duplicate Number */
/* Difficulty: Medium */

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int findDuplicate(vector<int> &nums)
    {
        for (int i = 0; i < nums.size(); i++)
        {
            int index = abs(nums[i]) - 1;
            if (nums[index] < 0)
            {
                return abs(nums[i]);
            }
            else
            {
                nums[index] *= -1;
            }
        }
        return 0;
    }
};