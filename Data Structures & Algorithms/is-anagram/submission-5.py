class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for i in s:
            s_dict[i] += 1
        for i in t:
            t_dict[i] += 1
        print(s_dict)
        print(t_dict)
        for key in s_dict.keys():
            if s_dict[key] != t_dict[key]:
                return False
        return True