class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            encoded_str += str(len(i))+"#"+i
        #print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        s_list = list(s)
        i = 0
        while s_list:
            if s_list[i] == "#":
                num = ""
                num_length = 1
                while i - num_length >= 0 and s_list[i-num_length].isdigit():
                    #print("made inside second while")
                    num+=s_list[i-num_length]
                    num_length +=1
                num = num[::-1]
                #print(num)
                num = int(num)
                append_str = ""
                for char in s_list[i+1:i+1+num]:
                    append_str+=char
                decoded_str.append(append_str)
                s_list= s_list[i+1+num:]
                #print("Updated s_list: ", s_list)
                i = 0
                num = ""
            else:
                i+=1
                #print(i)
        #print(decoded_str)
        return decoded_str