class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ans = [1]
        k = len(primes)
        pointers = [0] * k
        for _ in range(1, n):
            # find the next smallest value:
            options = []
            for j in range(k):
                options.append(ans[pointers[j]] * primes[j])
            selected = min(options)
            ans.append(selected)
            for j in range(k):
                if options[j] == selected:
                    pointers[j] += 1
        return ans[-1]


# heap

# to get the nth smallest ugly number, need to use a minHeap
# keep popping out n times
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        h = [1]
        for _ in range(n):
            curr = heapq.heappop(h)
            while h and h[0] == curr:
                curr = heapq.heappop(h)
            for prime in primes:
                heapq.heappush(h, prime * curr)
        return curr

# k merge with heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes:List[int]) -> int:
        h = []
        for prime in primes:
            h.append((prime, prime, 1))
        
        ugly = [1]
        pre = 1
        while n - 1 > 0:

            curr, prime, index = heapq.heappop(h)
            if pre != curr:
                ugly.append(curr)
                n -= 1
            
            heapq.heappush(h, (ugly[index] * prime, prime, index))

        return ugly[-1]
            