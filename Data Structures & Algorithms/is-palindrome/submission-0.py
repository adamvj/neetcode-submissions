class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = list(s)
        correctedForward = []
        for i in range(0, len(forward), 1):
            if forward[i].isalnum():
                correctedForward.append(forward[i].upper())
        backward = []
        for i in range(len(correctedForward)-1, -1, -1):
            backward.append(correctedForward[i].upper())
        if correctedForward == backward:
            return True
        return False