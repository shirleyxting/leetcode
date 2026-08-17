# Last updated: 8/16/2026, 9:53:28 PM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # DFS + backtracking
        # each step only has two choices: ( or )
        # rules: #_left <= n;  #_left >= #_right

        result = []

        def backtrack(path: list[str], left_count: int, right_count: int) -> None:
            # exit
            if len(path) == 2 * n:
                result.append("".join(path))
                return
            
            if left_count < n:
                path.append("(")
                backtrack(path, left_count + 1, right_count)
                path.pop()
            
            if left_count > right_count:
                path.append(")")
                backtrack(path, left_count, right_count + 1)
                path.pop()
        

        backtrack([], 0, 0)
        return result