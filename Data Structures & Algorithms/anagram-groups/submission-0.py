class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        visited = set() # Track indices we've already grouped
        
        for i in range(len(strs)):
            if i in visited:
                continue
            
            sublist = [strs[i]]
            visited.add(i)
            
            # Use len(strs) to ensure we hit the last element
            for j in range(i + 1, len(strs)):
                if j not in visited:
                    # Logic: If they are anagrams, add to sublist and mark as visited
                    if len(strs[i]) == len(strs[j]) and sorted(strs[i]) == sorted(strs[j]):
                        sublist.append(strs[j])
                        visited.add(j)
            
            results.append(sublist)
            
        return results