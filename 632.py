# the smallest range's high low limit should be numbers in the list
# the problem can be transferred as select one number from each list, to get the smallest diff of these numbers
# build a minHeap to with fixed size of k with element form of (value, col, row), each time move the smallest values col forward, since the list is non-decreasing.
# use a variable to record the max value
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h = [(vec[0], 0, i) for i, vec in enumerate(nums)]
        heapq.heapify(h)
        ansL = h[0][0]
        ansR = max(h)[0]
        maxValue = ansR
        while True:
            minValue, col, row = heapq.heappop(h)

            if maxValue - minValue < ansR - ansL:
                ansL = minValue
                ansR = maxValue

            if col + 1 == len(nums[row]):
                return [ansL, ansR]

            heapq.heappush(h, (nums[row][col + 1], col + 1, row))

            if nums[row][col + 1] > maxValue:
                maxValue = nums[row][col + 1]
