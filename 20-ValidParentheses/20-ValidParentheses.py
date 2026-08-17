# Last updated: 8/16/2026, 9:53:32 PM
class Solution:
    def isValid(self, s: str) -> bool:
        # stack to save left bracket, meet right brack, pop()
        # if matching, continue, else return False

        stack = []
        pair = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c not in pair: # left bracket, add to stack
                stack.append(c)
            else: # right bracket, pop() to check
                # if stack is empty OR pop() value mismatch -> false
                if not stack or stack.pop() != pair[c]:
                    return False
        
        # empty stack ->  pass
        return not stack