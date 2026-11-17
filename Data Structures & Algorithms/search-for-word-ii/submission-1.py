class TrieNode:
    def __init__(self) -> None:
        self.chilren = {}
        self.leaf = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordTrie = TrieNode()
        cur = wordTrie
        for word in words:
            cur = wordTrie
            for char in word:
                if char not in cur.chilren:
                    cur.chilren[char] = TrieNode()
                cur = cur.chilren[char]
            cur.leaf = True
        
        row, col = len(board), len(board[0])
        res, visited = set(), set()
        def dfs(x, y, node, word):
            if x < 0 or x >= row or y < 0 or y >= col or (x, y) in visited or board[x][y] not in node.chilren:
                return False
            
            visited.add((x, y))
            node = node.chilren[board[x][y]]
            word += board[x][y]
            if node.leaf:
                res.add(word)
            
            dfs(x + 1, y, node, word)
            dfs(x - 1, y, node, word)
            dfs(x, y + 1, node, word)
            dfs(x, y - 1, node, word)

            visited.remove((x, y))
        
        for i in range(row):
            for j in range(col):
                dfs(i, j, wordTrie, "")
        
        return list(res)