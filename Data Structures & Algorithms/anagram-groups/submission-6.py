class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = defaultdict(list)
        for item in strs:
            key = "".join(sorted(item))
            sorted_strs[key].append(item)
        return list(sorted_strs.values())
            

