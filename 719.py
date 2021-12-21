# defind a minHeap to hold all the pathforward.
# the element to save in minHeap is (value, pointers) pair, and the pointers are current location of each pointer in each row, and here the pointers format is tuple so that it can be saved as the key in hashset.
# need a seen hashset to filter/bypass the same results

import heapq


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        row = len(mat)
        col = len(mat[0])

        currPointers = [0] * row
        currSum = sum([vec[0] for vec in mat])
        h = [(currSum, tuple(currPointers))]
        seen = set(h)
        for _ in range(k):
            currSum, currPointers = heapq.heappop(h)
            for i, pointer in enumerate(currPointers):
                if pointer + 1 < col:
                    newSum = currSum - mat[i][pointer] + mat[i][pointer + 1]
                    newPointers = list(currPointers).copy()
                    newPointers[i] += 1
                    newItem = (newSum, tuple(newPointers))
                    if newItem not in seen:
                        heapq.heappush(h, newItem)
                        seen.add(newItem)
        return currSum
