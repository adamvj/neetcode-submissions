class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for today, today_temp in enumerate(temperatures):
            while stack and today_temp > temperatures[stack[-1]]:
                past_day = stack.pop()
                result[past_day] = today-past_day
            stack.append(today)
        return result