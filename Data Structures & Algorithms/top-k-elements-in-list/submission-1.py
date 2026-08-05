class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounts = defaultdict(int)
        for num in nums:
            numCounts[num] +=1
        print(numCounts)
        sortedKeys = sorted(numCounts, key=numCounts.get, reverse = True)
        sortedDict = {key: numCounts[key] for key in sortedKeys}
        sortedList = list(sortedDict.keys())
        return sortedList[0:k]