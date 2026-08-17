# Last updated: 8/16/2026, 9:47:34 PM
class Allocator:

    def __init__(self, n: int):
        # 0 means free
        self.memory = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        count = 0
        for i in range(len(self.memory)):
            if self.memory[i] == 0:
                count += 1
                if count == size:
                    # get the enough size, and continuous, set the previous set size to occupied
                    start = i - size + 1
                    for j in range(start, i+1):
                        self.memory[j] = mID
                    return start
            else:
                # reset count when meet occupied 
                count = 0
        
        return -1
            

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for i in range(len(self.memory)):
            if self.memory[i] == mID:
                self.memory[i] = 0
                freed += 1
        
        return freed
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)