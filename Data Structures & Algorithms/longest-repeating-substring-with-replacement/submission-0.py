class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        count_array = [0]*26
        for r in range(len(s)):
            count_array[ord(s[r])-65] +=1
            while (r-l+1) - max(count_array) > k:
                count_array[ord(s[l])-65] -=1
                l+=1
            longest = max(longest, r-l+1)
        return longest



        