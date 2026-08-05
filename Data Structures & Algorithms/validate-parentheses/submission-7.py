class Solution:
    def isValid(self, s: str) -> bool:
        parenth_map = {")":"(", "]":"[", "}":"{"}
        
        stack = []
        for item in s:
            if item in parenth_map:
                if not stack:
                    return False
                top = stack.pop()
                print("popped", top)
                if parenth_map[item] != top:
                    return False
            else:
                stack.append(item)
                print(stack)
        if not stack:
            return True
        return False