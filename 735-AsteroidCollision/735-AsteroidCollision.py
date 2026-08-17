# Last updated: 8/16/2026, 9:49:25 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack: alive asteroids
        # new compares with stack[-1]
        stack = []

        for asteroid in asteroids:
            alive = True

            # Collision: only stack fly towards right, and new asteroid fly towards left
            while stack and (stack[-1] > 0 and asteroid < 0) and alive:
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    alive = False
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                else:
                    alive = False
            
            if alive:
                stack.append(asteroid)
        
        return stack