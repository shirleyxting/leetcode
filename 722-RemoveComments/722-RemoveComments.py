# Last updated: 8/16/2026, 9:49:29 PM
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        NORMAL, IN_COMMENT = range(2)
        state = NORMAL
        tokens, buf = [], []

        for line in source:
            i, n = 0, len(line)
            while i < n:
                if state == IN_COMMENT:
                    if line[i: i+2] == "*/":
                        state = NORMAL
                        i += 2
                    else:
                        i += 1
            
                else: # normal text
                    if line[i: i+2] == "/*":
                        state = IN_COMMENT
                        i += 2
                    elif line[i: i+2] == "//":
                        # skip the afterwards chars, as they are in-line comment
                        break
                    else:
                        buf.append(line[i])
                        i += 1
            
            # line processing completed.
            # check block comment, if its not in block comment, add buf to tokens
            if state == NORMAL and buf:
                tokens.append("".join(buf))
                buf = [] # reset buf

        if buf:
            tokens.append("".join(buf))
        return tokens
                


