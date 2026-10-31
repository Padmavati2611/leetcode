class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]

        def dfs(r, c):
            if dp[r][c]:
                return dp[r][c]

            dp[r][c] = 1

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and 0 <= nc < cols
                    and matrix[nr][nc] > matrix[r][c]):
                    dp[r][c] = max(dp[r][c], 1 + dfs(nr, nc))

            return dp[r][c]

        ans = 0

        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))

        return ans