# Last updated: 9/8/2026, 9:31:19 PM
1class RandomizedSet:
2
3    def __init__(self):
4        # no gaps, used for random to fetch item in equal possibility
5        self.vals: list[int] = []
6        # val -> idx in vals[], used for insert() check duplicates, remove() locate index
7        self.val_to_idx: dict[int, int] = {}
8
9    def insert(self, val: int) -> bool:
10        if val in self.val_to_idx:
11            return False
12        
13        self.val_to_idx[val] = len(self.vals)
14        self.vals.append(val)
15        return True
16        
17
18    def remove(self, val: int) -> bool:
19        # swap and pop
20        # swap val with the last item, then pop() -> O(1)
21        if val not in self.val_to_idx:
22            return False
23        
24        last_val = self.vals[-1]
25        i = self.val_to_idx[val]
26
27        self.vals[i] = last_val
28        self.val_to_idx[last_val] = i
29
30        self.vals.pop()
31        del self.val_to_idx[val]
32
33        return True
34
35        
36
37    def getRandom(self) -> int:
38        return random.choice(self.vals)
39
40
41# Your RandomizedSet object will be instantiated and called as such:
42# obj = RandomizedSet()
43# param_1 = obj.insert(val)
44# param_2 = obj.remove(val)
45# param_3 = obj.getRandom()