from typing import List
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        LOG = (n + 1).bit_length()

        st_max = [nums[:]]
        st_min = [nums[:]]

        j = 1
        while (1 << j) <= n:
            length = 1 << (j - 1)

            mx = [
                max(st_max[j - 1][i], st_max[j - 1][i + length])
                for i in range(n - (1 << j) + 1)
            ]
            mn = [
                min(st_min[j - 1][i], st_min[j - 1][i + length])
                for i in range(n - (1 << j) + 1)
            ]

            st_max.append(mx)
            st_min.append(mn)
            j += 1

        def value(l: int, r: int) -> int:
            length = r - l + 1
            p = length.bit_length() - 1

            mx = max(st_max[p][l], st_max[p][r - (1 << p) + 1])
            mn = min(st_min[p][l], st_min[p][r - (1 << p) + 1])

            return mx - mn

        heap = []

        for l in range(n):
            r = n - 1
            heapq.heappush(heap, (-value(l, r), l, r))

        ans = 0

        for _ in range(k):
            v, l, r = heapq.heappop(heap)
            ans += -v

            if r > l:
                heapq.heappush(heap, (-value(l, r - 1), l, r - 1))

        return ans