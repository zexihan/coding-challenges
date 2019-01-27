from collections import deque
# Two Queues, push - O(1), pop O(n)
class MyStack_1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        self.top_element = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q1.append(x)
        self.top_element = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.q1) > 1:
            self.top_element = self.q1.popleft()
            self.q2.append(self.top_element)
        res = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.top_element

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return False if len(self.q1) > 0 else True


# Two Queues, push - O(n), pop O(1)
class MyStack_2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        self.top_element = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q2.append(x)
        self.top_element = x
        while len(self.q1) > 0:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        res = self.q1.popleft()
        if len(self.q1) > 0:
            self.top_element = self.q1[0]
        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.top_element

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return False if len(self.q1) > 0 else True



# One Queue, push - O(n), pop O(1)
class MyStack_3:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.append(x)
        n = len(self.q)
        while n > 1:
            self.q.append(self.q.popleft())
            n -= 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return False if len(self.q) > 0 else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
