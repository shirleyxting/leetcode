# Last updated: 8/16/2026, 9:53:41 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if len(strs) == 0: return ''
        # if len(strs) == 1: return strs[0]
        # res = []
        # size = len(strs)

        # for i in range(len(strs[0])):
        #     for j in range(size - 1):
        #         flag = False
        #         if len(strs[j]) > i and len(strs[j + 1]) > i and strs[j][i] ==  strs[j+1][i]:
        #             flag = True
        #         else:
        #             break
        #     if flag:
        #         res.append(strs[j][i])
        #     else:
        #         break
        
        # return ''.join(res)

        # no need for flag, if not match, directly return current visited strs[0]
        # for strs[0], check each char with following items
        if len(strs) == 0: return ''

        for i in range(len(strs[0])):
            c = strs[0][i]
            for item in strs[1:]:
                if i >= len(item) or c != item[i]:
                    # return so far visited chars in strs[0]
                    return strs[0][:i]
        # finish iterating strs[0], every char matched
        return strs[0]

                

