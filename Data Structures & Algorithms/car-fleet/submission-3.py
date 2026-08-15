class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair and sort descending by start position: O(n log n)
        pair = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for pos, spd in pair: # O(n)
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
                
        return len(stack)