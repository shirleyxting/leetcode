# Last updated: 8/16/2026, 9:52:57 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # add from right to left, keep record of carry value, at the end, reverse the string
        
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0: sum += int(a[i])
            if j >= 0: sum += int(b[j])

            # if sum >= 2:
            #     carry = 1
            #     res.append(sum - 2)
            # else:
            #     carry = 0
            #     res.append(sum)

            # use the binary feature, relation of 2
            carry = sum // 2
            res.append(sum % 2)

            i -= 1
            j -= 1
            
        if carry == 1: res.append(carry)

        # reverse res:
        return "".join(str(n) for n in reversed(res))
            


