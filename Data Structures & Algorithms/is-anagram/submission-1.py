class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        worddict = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in worddict:
                worddict[i] = s.count(i)
        for j in t:
            if j not in worddict:
                return False
            else:
                if t.count(j) != worddict[j]:
                    return False
        return True