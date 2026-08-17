# Last updated: 8/16/2026, 9:49:16 PM
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # actually its STACK, FILO
        new_s_list, new_t_list = [], []

        for char in s:
            if char == '#': 
                new_s_list = new_s_list[:-1]
            else:
                new_s_list.append(char)
        
        new_s = ''.join(new_s_list)

        for char in t:
            if char == '#': 
                new_t_list = new_t_list[:-1]
                # do not use pop(), as it will cause pop in empty list
            else:
                new_t_list.append(char)
        
        new_t = ''.join(new_t_list)

        return new_s == new_t
        
        