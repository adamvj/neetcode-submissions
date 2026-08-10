class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found_characters = []
        high_streak = 0
        streak = 0
        for i in range(len(s)):
            #print("current character: ", s[i])
            if s[i] not in found_characters:
                found_characters.append(s[i])
                streak +=1
            else:
                #print("Current found: ", found_characters)
                #print("Current streak", streak)
                #print("Current high_streak", high_streak)
                high_streak = max(high_streak, streak)
                #print(high_streak)
                idx = found_characters.index(s[i])
                found_characters = found_characters[idx+1:]
                found_characters.append(s[i])
                streak = len(found_characters)
                #print("adjustment: ", s[i])
            high_streak = max(high_streak, streak)
        return high_streak