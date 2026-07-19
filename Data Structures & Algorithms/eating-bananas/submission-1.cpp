#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int minEatingSpeed(vector<int> &piles, int h)
    {
        int largest = 0;
        for (int pile : piles)
        {
            largest = max(pile, largest);
        }
        int bottom = 1;
        int k;
        while (bottom <= largest)
        {
            int speed = (bottom + largest) / 2;
            int time = 0;
            for (int pile : piles)
            {
                time += pile / speed;
                if (pile % speed != 0)
                {
                    time++;
                }
            }
            if (time < h)
            {
                k = speed;
                largest = speed - 1;
            }
            if (time > h)
            {
                bottom = speed + 1;
            }
            if (time == h)
            {
                k = speed;
                largest--;
            }
        }
        return k;
    }
};
