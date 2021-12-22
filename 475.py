## heater 


import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        r = 0
        heaters.sort()

        for house in houses:

            idx = bisect.bisect_left(heaters, house)

            if idx == 0:
                r = max(r, heaters[idx] - house)
            elif idx == len(heaters):
                r = max(r, house - heaters[idx])
            else: 
                r = max(r, min(house - heaters[idx - 1], heaters[idx] - house))
        
        return r


# lighting, only k lights, you can assign position

class Solution:
    def findRadius(self, houses: list[int], lights: int) -> int:
        

        def valid(d):
            start = houses[0]
            end = start + d
            for _ in range(lights):
                idx = bisect.bisect_right(houses, end)
                if idx >= len(houses):
                    return True
                start = houses[idx]
                end = start + d
            return False


        houses.sort()

        l = 0
        r = houses[-1] - houses[0] + 1
        
        while l + 1 != r:

            mid = (l + r) // 2

            if valid(mid):
                r = mid
            else:
                l = mid
        
        return r / 2