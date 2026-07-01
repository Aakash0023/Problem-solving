class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows = defaultdict(int)
        cols = defaultdict(int)
        diag = defaultdict(int)      # r - c
        anti = defaultdict(int)      # r + c
        lampset = set()

        for r, c in lamps:
            if (r, c) not in lampset:
                lampset.add((r, c))
                rows[r] += 1
                cols[c] += 1
                diag[r - c] += 1
                anti[r + c] += 1

        ans = []

        for r, c in queries:
            if rows[r] > 0 or cols[c] > 0 or diag[r - c] > 0 or anti[r + c] > 0:
                ans.append(1)
            else:
                ans.append(0)

            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in lampset:
                        lampset.remove((nr, nc))
                        rows[nr] -= 1
                        cols[nc] -= 1
                        diag[nr - nc] -= 1
                        anti[nr + nc] -= 1

        return ans