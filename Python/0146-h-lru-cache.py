class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict()
        self.key = []
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.key.remove(key)
            self.key.insert(0,key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            self.key.remove(key)
            self.key.insert(0,key)
        elif len(self.cache) == self.capacity:
            old_key = self.key.pop()
            self.cache.pop(old_key)
            self.key.insert(0,key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.key.insert(0,key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)