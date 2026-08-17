# Last updated: 8/16/2026, 9:52:36 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # # p.val = q.val, true=isSameTree(p.left, q.left), true=isSameTree(p.right, q.right)

        # if not p and not q: return True
        # if (not p and q) or (p and not q): return False
        # if p.val != q.val: return False

        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)   

        # Method2 - BFS
        if not p and not q: return True
        if (not p and q) or (p and not q): return False

        p_queue, q_queue = deque(), deque()
        p_queue.append(p)
        q_queue.append(q)

        while p_queue and q_queue:
            i = p_queue.popleft()
            j = q_queue.popleft()
            
            if (not i and j) or (i and not j): 
                return False
            elif (i and j) and (i.val != j.val): 
                return False
            elif (i and j) and (i.val == j.val):
                p_queue.append(i.left)
                p_queue.append(i.right)
                q_queue.append(j.left)
                q_queue.append(j.right)
        
        if p_queue or q_queue: return False

        return True

