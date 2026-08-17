# Last updated: 8/16/2026, 9:51:59 PM

# class Node:
#     __slots__ = ("key", "val", "prev", "next")
#     def __init__(self, key=0, val=0):
#         self.key, self.val = key, val
#         self.prev = self.next = None

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.map = {}  # key -> node
#         # two sentinel nodes
#         self.head, self.tail = Node(), Node()
#         self.head.next, self.tail.prev = self.tail, self.head

#     def _remove(self, node: Node) -> None:
#         node.prev.next, node.next.prev = node.next, node.prev

#     def _add_to_front(self, node: Node) -> None:
#         # process node first, then head and head.next
#         node.next, node.prev = self.head.next, self.head
#         self.head.next.prev = node # this should proceed first than the next line
#         self.head.next = node

#     def get(self, key: int) -> int:
#         if key not in self.map:
#             return -1

#         node = self.map.get(key)
#         # recently visited: remove and than move node to head
#         self._remove(node)
#         self._add_to_front(node)

#         return node.val

#     def put(self, key: int, val: int) -> None:
#         if key in self.map:
#             # if exist before, remove it
#             self._remove(self.map[key])

#         node = Node(key, val)
#         # put in the front
#         self._add_to_front(node)
#         self.map[key] = node

#         # if exceed capacity, remove the last node
#         if len(self.map) > self.capacity:
#             lru = self.tail.prev
#             self._remove(lru)
#             del self.map[lru.key]
        


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)



# use OrderedDict
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.od = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        # move key to the end (recently visited/inserted)
        self.od.move_to_end(key)
        return self.od[key]
    
    def put(self, key: int, val: int) -> None:
        if key in self.od:
            self.od.move_to_end(key)
            self.od[key] = val
            return

        # evit the LRU first, then add new key
        if len(self.od) >= self.capacity:
            # evict LRU item
            self.od.popitem(last=False)
        
        self.od[key] = val
        
        

