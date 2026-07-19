class Solution
{
public:
    unordered_map<string, vector<string>> edgeMap;
    unordered_set<string> visited;
    int ladderLength(string beginWord, string endWord, vector<string> &wordList)
    {
        vector<string> all_words = vector<string>(wordList);
        all_words.push_back(beginWord);
        for (int i = 0; i < all_words.size() - 1; i++)
        {
            for (int j = i + 1; j < all_words.size(); j++)
            {
                string word1 = all_words[i];
                string word2 = all_words[j];

                int diff = 0;
                for (int i = 0; i < word1.size(); i++)
                {
                    if (diff > 1)
                    {
                        break;
                    }
                    if (word1[i] != word2[i])
                    {
                        diff += 1;
                    }
                }
                if (diff == 1)
                {
                    edgeMap[word1].push_back(word2);
                    edgeMap[word2].push_back(word1);
                }
            }
        }

        queue<string> q;
        q.push(beginWord);
        int length = 1;
        while (!q.empty())
        {
            int size = q.size();
            for (int i = 0; i < size; i++)
            {
                string curr = q.front();
                q.pop();
                visited.insert(curr);

                if (curr == endWord)
                {
                    return length;
                }
                for (string adj : edgeMap[curr])
                {
                    if (!visited.count(adj))
                    {
                        q.push(adj);
                    }
                }
            }
            length += 1;
        }
        return 0;
    }
};