# Last updated: 9/8/2026, 10:50:28 PM
1class MyHashMap:
2    # choose a prime numer "size", hasing func: key % size
3    # for same hash values, (key, val) saves in a bucket
4
5    def __init__(self):
6        self.size = 1009
7        self.buckets: list[list[list[int]]] = [ [] for _ in range(self.size)  ]
8    
9    def _index(self, key: int) -> int:
10        # hashing func, convert key into [0, size)
11        return key % self.size
12        
13
14    def put(self, key: int, value: int) -> None:
15        bucket = self.buckets[self._index(key)]
16
17        for pair in bucket:
18            if pair[0] == key:
19                pair[1] = value
20                return
21        
22        bucket.append([key, value])
23
24
25    def get(self, key: int) -> int:
26        bucket = self.buckets[self._index(key)]
27
28        for pair in bucket:
29            if pair[0] == key:
30                return pair[1]
31        
32        return -1
33        
34
35    def remove(self, key: int) -> None:
36        bucket = self.buckets[self._index(key)]
37
38        for i, pair in enumerate(bucket):
39            if pair[0] == key:
40                bucket.pop(i)
41                return
42        
43
44
45# Your MyHashMap object will be instantiated and called as such:
46# obj = MyHashMap()
47# obj.put(key,value)
48# param_2 = obj.get(key)
49# obj.remove(key)