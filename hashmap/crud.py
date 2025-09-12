class MyHashMap:
    def __init__(self):
        self.size = 100
        self.buckets = [[] for _ in range(self.size)]
    
    def put(self, key, value):
        index = hash(key) % self.size
        for i, (k,v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return 
        self.buckets[index].append((key, value))

    def get(self, key):
        index = hash(key) % self.size
        for (k,v) in self.buckets[index]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        index = hash(key) % self.size
        for i, (k,v) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]
                return

    def is_empty(self):
        return all(len(bucket) == 0 for bucket in buckets)


# Create HashMap
h = MyHashMap()

# Test put and get
h.put("apple", 5)
print(h.get("apple"))      # Output: 5

h.put("apple", 8)
print(h.get("apple"))      # Output: 8  (update test)

h.put("banana", 3)
print(h.get("banana"))     # Output: 3

print(h.get("carrot"))     # Output: -1 (does not exist)

# Test remove
h.remove("apple")
print(h.get("apple"))      # Output: -1 (after removal)

# Test is_empty
print(h.is_empty())        # Output: False (since "banana" still present)
h.remove("banana")
print(h.is_empty())        # Output: True
