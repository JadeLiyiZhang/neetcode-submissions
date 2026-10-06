from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def canChange(s1, s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
                if count > 1:
                    return False
            return True
        
        q = deque([(beginWord, 1)])
        seen = set()
        while q:
            current_word, cur_step = q.popleft()
            print(current_word)
            seen.add(current_word)
            if current_word == endWord:
                return cur_step
            for word in wordList:
                if word in seen:
                    continue
                if canChange(current_word, word):
                    q.append((word, cur_step + 1))
        return 0


