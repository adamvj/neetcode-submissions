class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        
        while i < len(s):
            # Find the position of the next '#' delimiter
            j = i
            while s[j] != "#":
                j += 1
            
            # Read length integer before '#'
            length = int(s[i:j])
            
            # Read 'length' characters after '#'
            decoded_str.append(s[j + 1 : j + 1 + length])
            
            # Advance pointer past length, '#', and the string content
            i = j + 1 + length
            
        return decoded_str