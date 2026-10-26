
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        if not board or not board[0]:
            return []

        trie = {}

        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node["$"] = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, parent):
            char = board[r][c]

            if char not in parent:
                return

            node = parent[char]

            word = node.pop("$", None)
            if word is not None:
                result.append(word)

            board[r][c] = "#"

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] != "#"
                ):
                    dfs(nr, nc, node)

            board[r][c] = char

            if not node:
                parent.pop(char)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return result
