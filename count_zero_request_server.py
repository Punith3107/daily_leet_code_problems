class Solution:
    def countServers(self, n, logs, x, queries):
        from collections import defaultdict
        logs.sort(key=lambda a: a[1])
        q = sorted((t, i) for i, t in enumerate(queries))
        d, l, r, ans = defaultdict(int), 0, 0, [0]*len(q)

        for t, i in q:
            while r < len(logs) and logs[r][1] <= t:
                d[logs[r][0]] += 1
                r += 1
            while l < r and logs[l][1] < t-x:
                d[logs[l][0]] -= 1
                if not d[logs[l][0]]:
                    del d[logs[l][0]]
                l += 1
            ans[i] = n-len(d)
    return ans
