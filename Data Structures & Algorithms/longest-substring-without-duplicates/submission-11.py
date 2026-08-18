class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        result = []
        for i in range(len(s)):
            if s[i] not in result:
                result.append(s[i])
                #print("Result when no duplicate: ", result)
                longest = max(longest, len(result))
            else:
                #print("Result when duplicate duplicate: ", result, "\n duplicate: ", s[i])
                dup_index = result.index(s[i])
                if dup_index == len(result)-1:
                    result = []
                else:
                    result = result[dup_index+1: ]
                result.append(s[i])
                #print("Result with duplicate updated: ", result)
        return longest