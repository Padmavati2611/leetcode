
from collections import Counter
from functools import lru_cache

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        colors = "RYBGW"
        hand_count = Counter(hand)

        def remove_groups(board):
            while True:
                stack = []

                for ball in board:
                    if stack and stack[-1][0] == ball:
                        stack[-1][1] += 1
                    else:
                        stack.append([ball, 1])

                new_board = "".join(
                    color * count
                    for color, count in stack
                    if count < 3
                )

                if new_board == board:
                    return board

                board = new_board

        @lru_cache(None)
        def dfs(board, hand_state):
            if not board:
                return 0

            answer = float("inf")

            for color_index, color in enumerate(colors):
                if hand_state[color_index] == 0:
                    continue

                new_hand = list(hand_state)
                new_hand[color_index] -= 1
                new_hand = tuple(new_hand)

                for i in range(len(board) + 1):

                    # Insert next to a ball of the same color
                    same_color = (
                        (i < len(board) and board[i] == color)
                        or
                        (i > 0 and board[i - 1] == color)
                    )

                    # Special case:
                    # Insert a different color between two
                    # adjacent balls of the same color
                    between_same = (
                        0 < i < len(board)
                        and board[i - 1] == board[i]
                        and board[i] != color
                    )

                    if not same_color and not between_same:
                        continue

                    # Avoid duplicate insertions within a run
                    if i > 0 and board[i - 1] == color:
                        continue

                    new_board = (
                        board[:i] + color + board[i:]
                    )

                    new_board = remove_groups(new_board)

                    result = dfs(new_board, new_hand)

                    if result != -1:
                        answer = min(answer, result + 1)

            return -1 if answer == float("inf") else answer

        board = remove_groups(board)

        return dfs(
            board,
            tuple(hand_count[color] for color in colors)
        )
