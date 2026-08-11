class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = 0
        s1list = list(s1)
        s1listcopy = s1list.copy()
        counter = 0
        checker = len(s1)
        while r < len(s2):
            if s2[r] in s1listcopy:
                s1listcopy.remove(s2[r])
                counter+=1
                if counter == checker:
                    return True
                r+=1
            else:
                s2 = s2[1:]
                r = 0
                counter = 0
                s1listcopy = s1list.copy()
        return False