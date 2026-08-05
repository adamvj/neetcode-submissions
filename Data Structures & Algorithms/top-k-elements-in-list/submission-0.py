class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            num_freq[num] = 1 + num_freq.get(num, 0)
        sorted_frequencies = sorted(num_freq.items(), key = lambda item: item[1], reverse=True)

        results = []
        for i in range(k):
            results.append(sorted_frequencies[i][0])
        
        return results