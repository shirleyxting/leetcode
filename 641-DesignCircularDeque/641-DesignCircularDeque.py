# Last updated: 9/15/2026, 9:19:13 PM
1class MyCircularDeque:
2    # use circular list
3    # keep record of frout index, and the actual len (as count of active items)
4    # then the end index = front + count - 1
5
6    def __init__(self, k: int):
7        self.arr = [0] * k
8        self.capacity = k
9        self.front = 0
10        self.count = 0
11        
12    def insertFront(self, value: int) -> bool:
13        if self.isFull():
14            return False
15        # front left shift 1, (-1%3=2 canm achive the circular)
16        self.front = (self.front - 1) % self.capacity
17        self.arr[self.front] = value
18        self.count += 1
19        return True
20
21    def insertLast(self, value: int) -> bool:
22        if self.isFull():
23            return False
24        # we do not maintain end index, its from calculation
25        # do not forget circular 
26        end = (self.front + self.count) % self.capacity
27        self.arr[end] = value
28        self.count += 1
29        return True
30
31    def deleteFront(self) -> bool:
32        if self.isEmpty():
33            return False
34        # front right shift 1
35        self.front = (self.front + 1) % self.capacity
36        self.count -= 1
37        # no need to clear the value in arr, as its not longer in our active win: [front, end]
38        return True
39        
40
41    def deleteLast(self) -> bool:
42        if self.isEmpty():
43            return False
44        # we do not maintain end index
45        self.count -= 1
46        return True
47        
48
49    def getFront(self) -> int:
50        if self.isEmpty():
51            return -1
52        return self.arr[self.front]
53
54    def getRear(self) -> int:
55        if self.isEmpty(): 
56            return -1
57        end = (self.front + self.count - 1) % self.capacity
58        return self.arr[end]
59
60    def isEmpty(self) -> bool:
61        return self.count == 0
62
63    def isFull(self) -> bool:
64        return self.count >= self.capacity
65
66# Your MyCircularDeque object will be instantiated and called as such:
67# obj = MyCircularDeque(k)
68# param_1 = obj.insertFront(value)
69# param_2 = obj.insertLast(value)
70# param_3 = obj.deleteFront()
71# param_4 = obj.deleteLast()
72# param_5 = obj.getFront()
73# param_6 = obj.getRear()
74# param_7 = obj.isEmpty()
75# param_8 = obj.isFull()