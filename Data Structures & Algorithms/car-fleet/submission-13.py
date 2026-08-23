class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pairs = sorted(zip(position, speed), reverse = True)
        times = []
        #print(sorted_pairs)

        for pos, spd in sorted_pairs:
            time = (target-pos)/spd
            if not times or time > times[-1]:
                times.append(time)
        return len(times)
