# Last updated: 8/16/2026, 9:49:13 PM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # order cars by position DESC
        # get time = each car drive time to reach target (no blockers)
        # stack: each fleet drive time 
        # new car time < stack[-1]: catch it, no op
        #              >          : cannot catch it, push into stack as a new fleet

        stack = []

        cars = [(pos, sp) for pos, sp in zip(position, speed)]
        cars.sort(key=lambda x: -x[0])

        times = [(target - pos) / sp for pos, sp in cars]

        for time in times:
            if not stack:
                stack.append(time)
            elif time <= stack[-1]:
                # catch it
                continue
            else:
                # cannot catch it, create a new fleet
                stack.append(time)
        
        return len(stack)
        