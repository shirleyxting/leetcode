# Last updated: 9/3/2026, 5:13:41 PM
1# """
2# This is the interface that allows for creating nested lists.
3# You should not implement it, or speculate about its implementation
4# """
5#class NestedInteger:
6#    def isInteger(self) -> bool:
7#        """
8#        @return True if this NestedInteger holds a single integer, rather than a nested list.
9#        """
10#
11#    def getInteger(self) -> int:
12#        """
13#        @return the single integer that this NestedInteger holds, if it holds a single integer
14#        Return None if this NestedInteger holds a nested list
15#        """
16#
17#    def getList(self) -> [NestedInteger]:
18#        """
19#        @return the nested list that this NestedInteger holds, if it holds a nested list
20#        Return None if this NestedInteger holds a single integer
21#        """
22
23class NestedIterator:
24    # Using a stack to simulate recursion/DFS, 
25    # and requiring the processing order to be consistent with the original order, 
26    #  -> "push to stack in reverse order"
27
28    def __init__(self, nestedList: [NestedInteger]):
29        self.stack = list(reversed(nestedList))
30        
31    
32    def next(self) -> int:
33        # hasNext() ensure its int
34        return self.stack.pop().getInteger()
35        
36    
37    def hasNext(self) -> bool:
38        while self.stack:
39            top = self.stack[-1]
40            if top.isInteger():
41                return True
42            
43            # pop top and expand it, push to stack in reversed order
44            self.stack.pop()
45            self.stack.extend( reversed(top.getList()) )
46        
47        return False
48
49         
50
51# Your NestedIterator object will be instantiated and called as such:
52# i, v = NestedIterator(nestedList), []
53# while i.hasNext(): v.append(i.next())