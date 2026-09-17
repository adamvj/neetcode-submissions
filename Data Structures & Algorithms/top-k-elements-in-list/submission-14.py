class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] +=1
        order = sorted(num_dict.values(), reverse = True)
        pairs = []
        for key in num_dict:
            pairs.append([num_dict[key], key])
        pairs.sort()
        pairs = pairs[::-1]
        #print(pairs)

        result = []
        for i in range(k):
            result.append(pairs[i][1])
        
        return result