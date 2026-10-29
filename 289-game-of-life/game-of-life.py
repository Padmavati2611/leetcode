class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                live = 0

                for i in range(max(0, r - 1), min(rows, r + 2)):
                    for j in range(max(0, c - 1), min(cols, c + 2)):
                        if (i, j) != (r, c) and board[i][j] in (1, -1):
                            live += 1

                if board[r][c] == 1:
                    if live < 2 or live > 3:
                        board[r][c] = -1
                else:
                    if live == 3:
                        board[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1