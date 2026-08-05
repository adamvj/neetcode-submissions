class Solution:
    def isValid(self, s: str) -> bool:
        bracket_defs = {"]":"[", "}":"{", ")": "("}
        stack = []
        for item in s:
            if item in bracket_defs.keys():
                if stack != [] and stack[-1] == bracket_defs[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        if stack == []:
            return True
        return False

