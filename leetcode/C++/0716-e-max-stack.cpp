// Two stacks
class MaxStack {
private:
    vector<pair<int, int>> stack;
public:
    /** initialize your data structure here. */
    MaxStack() {
    }
    
    void push(int x) {
        int curMax;
        if (stack.empty())
            curMax = x;
        else
            curMax = max(peekMax(), x);
        stack.emplace_back(x, curMax);
    }
    
    int pop() {
        int ret = top();
        stack.pop_back();
        return ret;
    }
    
    int top() {
        return stack.back().first;
    }
    
    int peekMax() {
        return stack.back().second;
    }
    
    int popMax() {
        vector<int> stack2;
        int curMax = peekMax();
        while (top() != curMax)
            stack2.push_back(pop());
        pop();
        while (!stack2.empty()) {
            push(stack2.back());
            stack2.pop_back();
        }
        return curMax;
    }
};

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack* obj = new MaxStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->peekMax();
 * int param_5 = obj->popMax();
 */