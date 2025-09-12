class ChainingHashMap:
    def __init__(self, size=2):
        self.size = size
        self.buckets = [[] for _ in range(size)] #Chaining

    def put(self, key, value):
        index = hash(key) % self.size
        for i, (k,v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))
    
    def get(self, key):
        index = hash(key) % self.size
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return -1

    def remove(self, key):
    index = hash(key) % self.size
    for i, (k, v) in enumerate(self.buckets[index]):
        if k == key:
            del self.buckets[index][i]
            return


    
h = ChainingHashMap(size=2)
h.put(2, 'A')
h.put(4, 'B')
h.put(3, 'C') # 3 % 2 = 1
print(h.buckets)

print(h.get(2))  # 'A'
print(h.get(4))  # 'B'
print(h.get(3))  # 'C'

h.remove(4)
print(h.buckets)  # Only (2, 'A') left in first bucket
