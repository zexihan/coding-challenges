"""
queue
"""
import collections
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.q = collections.deque([[0, 0]]) # q: tail...head
        self.w, self.h = width, height
        self.size = 0
        self.food = food[::-1]

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        head = self.q[-1][:] # [:]: shallow copy
        if direction == "U": head[0] -= 1
        if direction == "L": head[1] -= 1
        if direction == "R": head[1] += 1
        if direction == "D": head[0] += 1
        if not (0 <= head[0] < self.h and 0 <= head[1] < self.w):
            return -1
        
        if self.food and self.food[-1] == head:
            self.food.pop()
            self.size += 1
        else:
            self.q.popleft()
            if head in self.q:
                return -1
        self.q.append(head)
        return self.size


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)