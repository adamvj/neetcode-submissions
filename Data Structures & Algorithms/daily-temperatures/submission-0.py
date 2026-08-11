class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1. Prepare the answer array filled with 0s (default if no warmer day is found)
        res = [0] * len(temperatures)
        
        # 2. Use a stack to keep track of day indices: [day_index]
        stack = []

        # 3. Go through each day one by one
        for today, today_temp in enumerate(temperatures):
            
            # While there are days waiting in the stack, AND today is warmer than the top day on the stack
            while stack and today_temp > temperatures[stack[-1]]:
                # Pop the past day off the stack
                past_day = stack.pop()
                
                # Calculate how many days passed between then and now
                res[past_day] = today - past_day
            
            # Put today's index onto the stack so it can wait for a warmer day
            stack.append(today)

        return res