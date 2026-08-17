# Last updated: 8/16/2026, 9:50:10 PM
from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val = {}
        self.key_to_freq = {}
        # freq -> orderedDict({key1, _}, {key2, _}, ...)
        self.freq_to_keys: dict[int, OrderedDict] = defaultdict(OrderedDict)

    def _bump_freq(self, key: int) -> None:
        freq = self.key_to_freq[key]
        # remove key from current freq bucket
        del self.freq_to_keys[freq][key]

        # update min_freq if curr_freq bucket is empty, and curr_freq = min_freq
        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        
        # add key to new freq bucket
        self.freq_to_keys[freq + 1][key] = None
        self.key_to_freq[key] += 1


    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        # bump freq for key
        self._bump_freq(key)

        return self.key_to_val[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_val:
            # update val
            self.key_to_val[key] = value
            self._bump_freq(key)
            return
        
        # evict LFU first, then add new key
        if len(self.key_to_val) >= self.capacity:
            # pop (evict_key, _) from the orderedDict(the first inserted)
            evict, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[evict]
            del self.key_to_freq[evict]
            
        # new key-val pair
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1


        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)