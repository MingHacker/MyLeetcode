# always using the bricks to climb buildings
# when there is not enough bricks, check previous steps, find the step which used the most bricks, then replace method by using ladder


class Solution:
    def furthestBuildingReach(self, bricks: int, ladders: int, heights: List[int]) -> int:
        steps = [] # max heap
        for i in range(len(heights)):
            curr = heights[i]
            if i > 0 and curr - prev > 0:
                bricks -= curr - prev
                heapq.heappush(steps, prev - curr)
                while bricks < 0 and ladders > 0 and steps:
                    ladders -= 1
                    bricks -= heapq.heappop(steps)
                if bricks < 0:
                    return i - 1
            prev = curr 
        return i