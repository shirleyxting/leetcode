# Last updated: 8/16/2026, 9:49:21 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force: O(n^2)
        # find first right item > curr -> monotonic stack
        # 维护一个存下标的栈，从左到右扫描温度数组。
        # 每来一个新的温度，只要它比栈顶那天的温度高，就说明栈顶那天"等到了更暖和的一天"—
        #    弹出栈顶，用i - 弹出的下标算出它等了几天，记进res

        stack = []
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            curr = temperatures[i]

            while stack and curr > temperatures[stack[-1]]:
                days = i - stack[-1]
                res[stack[-1]] = days

                stack.pop()
            
            stack.append(i)
        
        return res
