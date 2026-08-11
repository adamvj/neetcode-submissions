class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for today, today_temp in enumerate(temperatures):
            #print("Stack: ", stack)
            while stack and today_temp > temperatures[stack[-1]]:
                #print("today_temp: ", today_temp, "\n", "temp at top: ", temperatures[stack[-1]])
                past = stack.pop()
                #print("Popped", past)
                result[past] = today-past
                #print("Result: ", result) 
            stack.append(today)
        return result