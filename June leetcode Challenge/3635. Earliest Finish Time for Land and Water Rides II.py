class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def calc(start1, dur1, start2, dur2):
            min_end = min(s + d for s, d in zip(start1, dur1))

            ans = float('inf')
            for s, d in zip(start2, dur2):
                ans = min(ans, max(min_end, s) + d)

            return ans

        return min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration)
        )