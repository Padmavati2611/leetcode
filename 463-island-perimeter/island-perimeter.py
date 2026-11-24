class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Each land cell has 4 sides
                    perimeter += 4

                    # If the cell above is land, remove shared side
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2

                    # If the cell to the left is land, remove shared side
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2

        return perimeter