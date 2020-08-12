// One stack with pair
class MinStack {
private:
    vector<pair<int, int>> minStack;
public:
    /** initialize your data structure here. */
    MinStack() {
    }
    
    void push(int x) {
        if (minStack.empty())  
            minStack.emplace_back(x, x);
        else
            minStack.emplace_back(x, min(x, getMin()));
    }
    
    void pop() {
        minStack.pop_back();
    }
    
    int top() {
        return minStack.back().first;
    }
    
    int getMin() {
        return minStack.back().second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

// Two stacks
class MinStack {
private:
    vector<int> stack1;
    vector<int> stack2;
public:
    /** initialize your data structure here. */
    MinStack() {
    }
    
    void push(int x) {
        stack1.push_back(x);
        if (stack2.empty() || x <= getMin())
            stack2.push_back(x);
    }
    
    void pop() {
        if (getMin() == top()) 
            stack2.pop_back();
        stack1.pop_back();
    }
    
    int top() {
        return stack1.back();
    }
    
    int getMin() {
        return stack2.back();
    }
};
