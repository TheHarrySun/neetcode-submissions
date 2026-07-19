class Solution {
public:
    bool isValid(string s) {
        stack<char> close;
        stack<char> open;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                open.push(s[i]);
            }
            else if (!open.empty()) {
                char c = open.top();
                open.pop();
                if (s[i] == ')') {
                    if (c != '(') {
                        return false;
                    }
                }
                else if (s[i] == ']') {
                    if (c != '[') {
                        return false;
                    }
                }
                else {
                    if (c != '{') {
                        return false;
                    }
                }
            }
            else {
                return false;
            }
        }
        return open.empty();
    }
};
