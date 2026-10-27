class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.leaf = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            cur = root  # 每个单词从根节点开始
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.leaf = True  # 整个单词插入完成后标记

        row, col = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r < 0 or r >= row
                or c < 0 or c >= col
                or (r, c) in visit
                or board[r][c] not in node.children
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.leaf:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))

        for r in range(row):
            for c in range(col):
                dfs(r, c, root, "")

        return list(res)