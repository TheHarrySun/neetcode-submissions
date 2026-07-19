class Solution
{
public:
    int ladderLength(string beginWord, string endWord, vector<string> &wordList)
    {
        unordered_set<string> allWords;
        unordered_set<string> visited;
        for (string word : wordList)
        {
            allWords.insert(word);
        }

        queue<string> q;
        q.push(beginWord);
        int length = 0;
        while (!q.empty())
        {
            length += 1;
            int len = q.size();
            for (int i = 0; i < len; i++)
            {
                string curr = q.front();
                q.pop();
                visited.insert(curr);

                if (curr == endWord)
                {
                    return length;
                }

                for (int j = 0; j < curr.length(); j++)
                {
                    char original = curr[j];
                    for (char c = 'a'; c <= 'z'; c++)
                    {
                        curr[j] = c;
                        if (c == original)
                        {
                            continue;
                        }
                        if (allWords.count(curr) && !visited.count(curr))
                        {
                            q.push(curr);
                        }
                    }
                    curr[j] = original;
                }
            }
        }
        return 0;
    }
};