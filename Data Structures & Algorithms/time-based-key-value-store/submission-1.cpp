class TimeMap
{
public:
    unordered_map<string, map<int, string>> keys;
    TimeMap()
    {
    }

    void set(string key, string value, int timestamp)
    {
        keys[key].insert({timestamp, value});
    }

    string get(string key, int timestamp)
    {
        auto it = keys[key].upper_bound(timestamp);
        if (it == keys[key].begin())
        {
            return "";
        }
        else
        {
            return prev(it)->second;
        }
    }
};