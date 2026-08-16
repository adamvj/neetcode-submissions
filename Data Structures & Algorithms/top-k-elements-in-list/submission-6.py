class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = defaultdict(int)
        for i in nums:
            num_counts[i] +=1
        tuples_list = []
        for items in zip(list(num_counts.values()), list(num_counts.keys())):
            tuples_list.append(items)
        #print("tuples_list: ", tuples_list)
        tuples_list.sort()
        tuples_list = tuples_list[::-1]
        #print("sorted desc tuples_list: ", tuples_list)
        result = []
        for i in range(k):
            result.append(tuples_list[i][1])
        
        return result