class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        for segment in strs:
            encoded_strs += str(len(segment)) + "#" + segment
        print(encoded_strs)
        return encoded_strs
    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_strs = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            decoded_strs.append(s[j+1: j+1+length])
            i = j+1+length
        return decoded_strs
            