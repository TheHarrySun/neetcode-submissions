class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<string> seq;
        unordered_set<string> ops = {"+", "-", "/", "*"};
        for (string s : tokens) {
            if (ops.count(s)) {
                int second = stoi(seq.top());
                seq.pop();
                int first = stoi(seq.top());
                seq.pop();
                int result;
                if (s == "+") {
                    result = first + second;
                }
                else if (s == "-") {
                    result = first - second;
                }
                else if (s == "*") {
                    result = first * second;
                }
                else {
                    result = first / second;
                }
                seq.push(to_string(result));
            }
            else {
                seq.push(s);
            }
        }
        return stoi(seq.top());
    }
};
