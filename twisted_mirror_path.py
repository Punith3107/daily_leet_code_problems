class Solution:
    def uniquePaths(self, grid):
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if not dp[i][j]: continue
                if j+1 < n:
                    x, y = i, j+1
                    while x < m and y < n and grid[x][y]:
                        x += 1
                    if x < m and y < n:
                        dp[x][y] = (dp[x][y] + dp[i][j]) % MOD
                if i+1 < m:
                    x, y = i+1, j
                    while x < m and y < n and grid[x][y]:
                        y += 1
                    if x < m and y < n:
                        dp[x][y] = (dp[x][y] + dp[i][j]) % MOD

        return dp[-1][-1]
